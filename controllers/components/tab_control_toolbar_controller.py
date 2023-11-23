import requests
from PySide6.QtGui import QAction

from interfaces.structs import PreviewToolbarActionType, ProgramType
from models.explorer.program_item_model import ProgramItemModel
from models.settings.http_request_item import HTTPRequestItem
from models.signal_data_models import PreviewProgramData
from utils.signal_bus import signalBus
from views.components.tab_control_toolbar import TabControlToolbarView


class TabControlToolbarController(TabControlToolbarView):
    def __init__(self, itemModel: ProgramItemModel = None):
        super().__init__()

        self.__itemModel = itemModel

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        if self.__itemModel is None:
            return
        self.executeAction.setData(PreviewProgramData(PreviewToolbarActionType.EXECUTE, self.__itemModel))
        self.fetchAction.setData(PreviewProgramData(PreviewToolbarActionType.FETCH, self.__itemModel))

    # endregion

    # region - Configure
    def __configure(self):
        self.toolbar.actionTriggered.connect(self.__handleToolbarActions)

    # endregion

    # region - Event Handlers
    def __handleToolbarActions(self, action: QAction):
        actionData: PreviewProgramData = action.data()
        if actionData.procedure() == PreviewToolbarActionType.FETCH:
            self.fetchProgram(actionData.data())

        if actionData.procedure() == PreviewToolbarActionType.EXECUTE:
            self.executeProgram(actionData.data())

    # endregion

    # region - Workers
    def fetchProgram(self, data: ProgramItemModel):
        pass

    def executeProgram(self, data: ProgramItemModel):
        """
        handles execution of program.
        creates and configures a request. the request is sent to the manager and executed there
        the response is handled by the configured success function.
        :param data:
        :return:
        """
        url = 'http://localhost:8080/'
        if data.programType() == ProgramType.SCAN_ERLANG:
            url = f'http://localhost:8080/scan?nprocs={data.properties().nProcs()}'

        if data.programType() == ProgramType.REDUCE_ERLANG:
            url = f'http://localhost:8080/reduce?nprocs={data.properties().nProcs()}'

        httpRequest = HTTPRequestItem(url, data.programType(), "get")
        httpRequest.onError.connect(self.__handleError)
        httpRequest.onComplete.connect(self.__executeSuccessful)
        signalBus.onHTTPRequest.emit(httpRequest)

    def __executeSuccessful(self, response):
        signalBus.onLogToOutput.emit(str(type(response)))
        print(response)

    def __handleError(self, error):
        signalBus.onLogToOutput.emit(str(type(error)))
        print(error)

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters

    # endregion

    # region - Setters
    def setItemModel(self, item: ProgramItemModel):
        self.__itemModel = item
        self.__initialize()
    # endregion
