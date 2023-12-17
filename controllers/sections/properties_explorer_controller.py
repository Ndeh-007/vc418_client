from PySide6.QtGui import QIntValidator

from interfaces.structs import MenuBarActionType, AlertType
from models.common.execution_step_model import ExecutionStepModel
from models.common.execution_timeline_model import ExecutionTimelineModel
from models.explorer.program_item_model import ProgramItemModel
from models.explorer.program_properties_model import ProgramPropertiesModel
from models.common.signal_data_models import SystemRequestData, SystemRequest, SystemAlert
from models.explorer.properties_table_data_model import PropertiesTableDataModel
from models.explorer.properties_table_model import PropertiesTableModel
from utils.signal_bus import signalBus
from views.sections.properties_explorer import PropertyExplorerView

import store.settings as ss


class PropertyExplorerController(PropertyExplorerView):
    def __init__(self):
        super().__init__()
        self.__program: ProgramItemModel | None = None

        self.__executionTimelineTableModel: PropertiesTableModel | None = None
        self.__executionFrameSummaryModel: PropertiesTableModel | None = None

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # initially nothing has been selected
        # show the placeholder
        self.__showPlaceholder(True)

        #  update the contents of the various inputs
        if self.__program is None:
            return

        self.__initializeProperties(self.__program)

    # endregion

    # region - configure
    def __configure(self):

        self.currentPidSelectionInput.currentIndexChanged.connect(self.__handleTimelineSelectionChanged)

        # attach input validators to the inputs
        intValidator = QIntValidator()
        self.nProcsInput.setValidator(intValidator)

        # attach event handlers to inputs
        self.nProcsInput.textEdited.connect(self.__handleNProcsInputChanged)

        self.minimizeBtn.clicked.connect(self.__handleMinimizeBtnClicked)

    # endregion

    # region - event handlers
    def __handleTimelineSelectionChanged(self, index: int):
        pid = self.currentPidSelectionInput.itemText(index)
        timeline = self.__program.properties().executionTimeLine().get(pid)
        self.__updateExecutionTimeline(timeline)

    def __handleActiveProgramChanged(self, program: ProgramItemModel):

        if program is None:
            self.__showPlaceholder(True)
            return

        # change the values
        program = ss.APP_SETTINGS.PROGRAMS.activeProgram()
        self.__initializeProperties(program)

    def __handleNProcsInputChanged(self, _):
        value = self.nProcsInput.text()
        if value == "":
            return
        if int(value) < 2:
            alert = SystemAlert(f"Expected value greater than 2, got '{value}'", AlertType.Warning)
            signalBus.onSystemAlert.emit(alert)
            return
        self.__program.properties().setNProcs(int(value))
        ss.APP_SETTINGS.PROGRAMS.setActiveProgram(self.__program)

    def __handlePropertiesChanged(self):
        signalBus.onUpdateProgram.emit(self.__program)

    def __handleShowProgramDetailsSignal(self, item: ProgramItemModel | None):
        # if we have no data to update, show the placeholder
        if item is None:
            self.__showPlaceholder(True)
            return

        # read the data from store with the provided data.id()
        data = ss.APP_SETTINGS.PROGRAMS.activeProgram()

        if data is None:
            print("Data is None. [Location] (properties_explorer_controller)")
            return

        # update the local value
        self.__initializeProperties(data)

        # toggle the placeholder
        self.__showPlaceholder(False)

    def __handleUpdateTree(self, executionFrame: ExecutionStepModel):
        self.__updateExecutionFramesValues(executionFrame.frameIndex(), executionFrame)

    def __handleProgramDeleted(self, program: ProgramItemModel):
        """
        if program has been deleted by the user int the programs explorer, clear this sections data and show the
        placeholder
        :param program:
        :return:
        """
        if program.id() == self.__program.id():
            # clear the properties model so that we can call initialize on an empty model,
            # and then we toggle the placeholder
            self.__program.properties().clear()
            self.__initializeInputs(self.__program.properties())
            self.__showPlaceholder(True)

    @staticmethod
    def __handleMinimizeBtnClicked():
        d = SystemRequestData(MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER, MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER)
        r = SystemRequest(d)
        signalBus.onSystemRequest.emit(r)

    # endregion

    # region workers

    def __showPlaceholder(self, state: bool):
        """
        hides or shows the placeholder
        if state == true -> show else hide
        :param state:
        :return:
        """
        if state:
            self.contentLayout.setCurrentIndex(1)
        else:
            self.contentLayout.setCurrentIndex(0)

    def __updateExecutionFramesValues(self, index: int, executionFrame: ExecutionStepModel):
        # # update the frames values
        # update the labels
        self.currentFrameLabel.setText(str(index))
        self.totalFramesLabel.setText(str(len(self.__program.properties().executionFrames()) - 1))

        # update the table
        self.__executionFrameSummaryModel = PropertiesTableModel(executionFrame.propsTabelDataModel())
        self.executionFramePreviewTabel.setModel(self.__executionFrameSummaryModel)

    def __updateExecutionTimeline(self, timeline: ExecutionTimelineModel):
        if timeline is None:
            print("timeline is none, cannot render data in properties section")
            return
        self.currentPidLabel.setText(timeline.id())
        self.__executionTimelineTableModel = PropertiesTableModel(timeline.propsTabelDataModel())
        self.pidExecutionTimelineTable.setModel(self.__executionTimelineTableModel)

    def __initializeInputs(self, data: ProgramPropertiesModel):
        # update the n procs input
        self.nProcsInput.setText(str(data.nProcs()))

        # check if there are frames. if there are no frames, initialize empty values
        if len(data.executionFrames()) == 0:
            self.currentFrameLabel.setText("-")
            self.totalFramesLabel.setText("-")

            self.currentPidSelectionInput.clear()
            self.currentPidLabel.setText("-")

            self.__executionFrameSummaryModel = PropertiesTableModel(PropertiesTableDataModel({}, ["Property", "Value"]))
            self.executionFramePreviewTabel.setModel(self.__executionFrameSummaryModel)

            self.__executionTimelineTableModel = PropertiesTableModel(PropertiesTableDataModel({}, ["Frame", "Value"]))
            self.pidExecutionTimelineTable.setModel(self.__executionTimelineTableModel)
        else:
            self.currentPidSelectionInput.clear()
            keys = list(data.executionTimeLine().keys())
            self.currentPidSelectionInput.addItems(keys)
            self.__updateExecutionFramesValues(0, data.executionFrameAtIndex(0))
            self.__updateExecutionTimeline(data.executionTimeLine().get(self.__program.id()))

    def __initializeProperties(self, program: ProgramItemModel):
        # update the local value
        self.__program = program

        # update the label of the properties
        self.programTitleLabel.setText(program.text())

        # initialize the inputs in the properties section
        self.__initializeInputs(program.properties())
    # endregion

    # region - connect signals

    def __connectSignals(self):
        signalBus.onShowProgramProperties.connect(self.__handleShowProgramDetailsSignal)
        signalBus.onActiveProgramChanged.connect(self.__handleActiveProgramChanged)
        signalBus.onUpdateTree.connect(self.__handleUpdateTree)
        signalBus.onDeleteProgram.connect(self.__handleProgramDeleted)

    # endregion
