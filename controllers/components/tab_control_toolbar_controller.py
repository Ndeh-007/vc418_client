import json

from PySide6.QtGui import QAction

import store.settings as ss
from interfaces.structs import PreviewToolbarActionType, ProgramType
from models.common.execution_step_model import ExecutionStepModel
from models.common.signal_data_models import PreviewProgramData
from models.explorer.program_item_model import ProgramItemModel
from models.settings.http_request_item import HTTPRequestItem
from utils.helpers import parseJSONData
from utils.signal_bus import signalBus
from views.components.tab_control_toolbar import TabControlToolbarView


class TabControlToolbarController(TabControlToolbarView):
    def __init__(self, itemModel: ProgramItemModel = None):
        super().__init__()

        self.__itemModel = itemModel
        self.__executionFrames = []

        # reset the values of the playback to be initialized by the controller

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        self.playbackWidget.setFrameValue(0)
        self.playbackWidget.setFramesTotalValue(0)

        if self.__itemModel is None:
            return
        self.executeAction.setData(PreviewProgramData(PreviewToolbarActionType.EXECUTE, self.__itemModel))
        self.reloadAction.setData(PreviewProgramData(PreviewToolbarActionType.RELOAD, self.__itemModel))

    # endregion

    # region - Configure
    def __configure(self):
        self.toolbar.actionTriggered.connect(self.__handleToolbarActions)

        self.playbackWidget.nextBtn.clicked.connect(self.__handleNextFrame)
        self.playbackWidget.previousBtn.clicked.connect(self.__handlePreviousFrame)
        self.playbackWidget.playPauseBtn.clicked.connect(self.__handlePausePlayFrame)
        self.playbackWidget.onPlayerTimeout.connect(self.__handlePlayerTimerTimeout)

    # endregion

    # region - Event Handlers
    def __handleError(self, error):
        signalBus.onLogToOutput.emit(str(type(error)))
        print(error)

    def __handleLoadPlayer(self, frames: list[ExecutionStepModel]):
        """
        updates the execution frames and resets the values of the player
        :param frames:
        :return:
        """
        # update the execution frames
        self.__executionFrames = frames

        # update the player values
        self.playbackWidget.setFramesTotalValue(len(frames) - 1)
        self.playbackWidget.setFrameValue(0)

    def __handleNextFrame(self):
        """
        actions performed when the next button is clicked
        first it stops the playback thereby switching to manual mode and then executes from the currently defined frame
        index.
        :return:
        """
        self.playbackWidget.stopPlayback()
        self.__dispatchFrame(1)

    def __handlePreviousFrame(self):
        """
        actions performed when back button is pressed
        first it stops the playback thereby switching to manual mode and then executes from the currently defined frame
        index.
        :return:
        """
        self.playbackWidget.stopPlayback()
        self.__dispatchFrame(-1)

    def __handlePlayerTimerTimeout(self):
        """
        send the next frame on every count
        :return:
        """
        self.__dispatchFrame(1)

    def __handlePausePlayFrame(self):
        print(self.playbackWidget.playerState())
        if self.playbackWidget.isPaused():
            self.playbackWidget.startPlayback()
        else:
            self.playbackWidget.stopPlayback()

    def __handleProgramUpdate(self, item: ProgramItemModel):
        if item.id() != self.__itemModel.id():
            return
        self.__itemModel = item

    def __handleToolbarActions(self, action: QAction):
        actionData: PreviewProgramData = action.data()

        data = ss.APP_SETTINGS.PROGRAMS.programs(actionData.data().id())
        if data is None:
            signalBus.onLogErrorToOutput.emit("data not found for store. ")
            return

        self.__itemModel = data

        if actionData.procedure() == PreviewToolbarActionType.RELOAD:
            self.reloadProgram(data)

        if actionData.procedure() == PreviewToolbarActionType.EXECUTE:
            self.executeProgram(data)

    # endregion

    # region - Workers

    # region - Private Workers

    def __dispatchFrame(self, offsetValue: int):
        """
        offset and dispatch the frame
        :param offsetValue:
        :return:
        """
        idx = int(self.playbackWidget.frameValue()) + offsetValue
        if idx not in range(0, len(self.__executionFrames)):
            self.playbackWidget.stopPlayback()
            return
        self.playbackWidget.setFrameValue(idx)
        signalBus.onUpdateTree.emit(self.__executionFrames[idx])

    def __parseResponse(self, filePath: str):
        """
        parses the stored http response data and dispatches the data to the playback controller and to the canvas
        :param filePath:
        :return:
        """
        parsedData = parseJSONData(filePath)
        tree = parsedData.get("binaryTree")
        frames = parsedData.get("executionFrames")
        timelines = parsedData.get("executionTimelines")

        # update the local item model properties
        self.__itemModel.properties().setExecutionFrames(frames)
        self.__itemModel.properties().setExecutionTimelines(timelines)
        self.__itemModel.properties().setNProcs(tree.nProcs())

        # update the binary-tree's fileItemModel
        tree.setProgramItem(self.__itemModel)

        # dispatch data
        # update the active program in the store.
        ss.APP_SETTINGS.PROGRAMS.updateProgram(self.__itemModel.id(), self.__itemModel)

        # send to the player
        signalBus.onLoadPlayer.emit(frames)
        # send to canvas
        signalBus.onLoadTreeModel.emit(tree)

    def __executeSuccessful(self, response):
        """
        When the execution is successful, dump the response to the designated json file.
        After writing has been complete. initiate the rendering sequence
        :param response: the http response gotten from the request made
        :return:
        """
        # collect file path
        filePath = ss.APP_SETTINGS.CONFIGURATION.httpResponseJSONFile()
        # save to temporal location (required)
        with open(filePath, "w") as file:
            json.dump(response, file, indent=4)

        try:
            # parse the data
            self.__parseResponse(filePath)
        except Exception as e:
            signalBus.onLogErrorToOutput.emit(f"Failed to load data from json file with error => {str(e)}")

    # endregion

    # region - Public Workers

    def reloadProgram(self, data: ProgramItemModel):
        """
        loads the previous saved data from the temporal storage location
        :param data:
        :return:
        """
        filePath = ss.APP_SETTINGS.CONFIGURATION.httpResponseJSONFile()
        signalBus.onMakeProgramActive.emit(data)
        self.__parseResponse(filePath)

    def executeProgram(self, data: ProgramItemModel):
        """
        handles execution of program.
        creates and configures a request. the request is sent to the manager and executed there
        the response is handled by the configured success function.
        :param data:
        :return:
        """
        url = ss.APP_SETTINGS.SERVER.servers(data.serverID()).url()
        if data.programType() == ProgramType.SCAN_ERLANG:
            url = f'{url}scan?nprocs={data.properties().nProcs()}'

        if data.programType() == ProgramType.REDUCE_ERLANG:
            url = f'{url}reduce?nprocs={data.properties().nProcs()}'

        httpRequest = HTTPRequestItem(data.id(), url, data.programType(), "get")
        httpRequest.onError.connect(self.__handleError)
        httpRequest.onComplete.connect(self.__executeSuccessful)
        signalBus.onHTTPRequest.emit(httpRequest)

    # endregion

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        signalBus.onUpdateProgram.connect(self.__handleProgramUpdate)
        signalBus.onLoadPlayer.connect(self.__handleLoadPlayer)

    # endregion

    # region - Getters

    # endregion

    # region - Setters
    def setItemModel(self, item: ProgramItemModel):
        self.__itemModel = item
        self.__initialize()
    # endregion
