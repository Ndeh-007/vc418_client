from PySide6.QtGui import QAction

from interfaces.structs import PreviewToolbarActionType
from models.explorer.program_item_model import ProgramItemModel
from models.signal_data_models import PreviewProgramData
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
        # create and send http request.

        pass
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

