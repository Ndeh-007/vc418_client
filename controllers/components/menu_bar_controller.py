from typing import Callable, Any

from PySide6.QtGui import QAction

from interfaces.structs import MenuBarActionType, AlertType
from models.signal_data_models import SystemRequest, SystemAlert
from utils.signal_bus import signalBus
from views.components.menu_bar import MenuBarView


class MenuBarController(MenuBarView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__workerTable: dict[MenuBarActionType, Callable[..., Any]] = {}

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        """
        creates the worker table
        :return:
        """

        self.outputAction.setChecked(True)
        self.propsAction.setChecked(True)
        self.programAction.setChecked(True)

        self.__workerTable.update({
            MenuBarActionType.ABOUT: self.__openSettings,
            MenuBarActionType.EXIT: self.__killApplication,
            MenuBarActionType.SETTINGS: self.__openSettings,
            MenuBarActionType.START_SERVER: self.__startServer,
            MenuBarActionType.STOP_SERVER: self.__stopServer,
            MenuBarActionType.TOGGLE_OUTPUT_EXPLORER: self.__toggleSection,
            MenuBarActionType.TOGGLE_PROGRAMS_EXPLORER: self.__toggleSection,
            MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER: self.__toggleSection,
        })

    # endregion

    # region - Configure
    def __configure(self):
        self.triggered.connect(self.__handleMenuBarActionTriggered)

    # endregion

    # region - Event Handlers
    def __handleMenuBarActionTriggered(self, action: QAction):
        """
        gets the data from the action and pass it to the worker table handler
        :param action:
        :return:
        """

        # we handle the case if we are getting from the menu bar for only view toggling.
        if action.data() in [MenuBarActionType.TOGGLE_OUTPUT_EXPLORER, MenuBarActionType.TOGGLE_PROGRAMS_EXPLORER, MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER]:
            self.__fireToggleSection(action.data())
            return

        self.__workerTableHandler(action.data(), action.data())

    def __handleSystemWideRequests(self, signal: SystemRequest):
        """
        collect the signal data, extract the action and the content and pass
        to the worker table handler.
        :param signal:
        :return:
        """
        # the signal also carries the instruction scope, this maybe useful in the future
        # at the moment I am unsure.
        self.__workerTableHandler(signal.data().action, signal.data().content)

    # endregion

    # region - Worker Handler
    def __workerTableHandler(self, actionType: MenuBarActionType, content: Any):
        """
        calls required functions based on keys provided by the actionType
        :param actionType:
        :param content:
        :return:
        """
        try:
            task = self.__workerTable.get(actionType)
            task(content)
        except Exception as e:
            self.__signalError(f"Worker table Error: {str(e)}")

    # endregion

    # region - Workers
    def __startServer(self, _):
        self.__signalAlert("Server Started")

    def __stopServer(self, _):
        self.__signalAlert("Server Ended")

    def __openSettings(self, _):
        self.__signalAlert("Settings Opened")

    def __killApplication(self, _):
        self.__signalAlert("Application killed")

    def __toggleSection(self, action):
        if not isinstance(action, MenuBarActionType):
            self.__signalError(f"Invalid key in toggle section: Got {action}")
            return

        # trigger output section toggle
        if action == MenuBarActionType.TOGGLE_OUTPUT_EXPLORER:
            state = self.outputAction.isChecked()
            newState = not state
            self.outputAction.setChecked(newState)

        # trigger properties section toggle
        if action == MenuBarActionType.TOGGLE_PROGRAMS_EXPLORER:
            state = self.programAction.isChecked()
            newState = not state
            self.programAction.setChecked(newState)

        # trigger programs section toggle
        if action == MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER:
            state = self.propsAction.isChecked()
            newState = not state
            self.propsAction.setChecked(newState)

        self.__fireToggleSection(action)

    def __fireToggleSection(self, action):
        # trigger output section toggle
        if action == MenuBarActionType.TOGGLE_OUTPUT_EXPLORER:
            state = self.outputAction.isChecked()
            signalBus.onToggleOutputExplorer.emit(state)
            return

        # trigger properties section toggle
        if action == MenuBarActionType.TOGGLE_PROGRAMS_EXPLORER:
            state = self.programAction.isChecked()
            signalBus.onToggleProgramsExplorer.emit(state)
            return

        # trigger programs section toggle
        if action == MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER:
            state = self.propsAction.isChecked()
            signalBus.onTogglePropertiesExplorer.emit(state)
            return

    # endregion

    # region - Signaling
    @staticmethod
    def __signalAlert(message: str):
        alert = SystemAlert(message, AlertType.Event)
        signalBus.onSystemAlert.emit(alert)

    @staticmethod
    def __signalError(message: str):
        alert = SystemAlert(message)
        signalBus.onSystemAlert.emit(alert)

    def __connectSignals(self):
        signalBus.onSystemRequest.connect(self.__handleSystemWideRequests)

    # endregion
