from controllers.components.dialog.settings_explorer_dialog_controller import SettingsExplorerDialogController
from models.settings.http_request_manager import HTTPRequestManager
from models.settings.process_manager import ProcessManager
from utils.signal_bus import signalBus
from views.pages.home_page import HomePageView


class HomePageController(HomePageView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.httpManager = HTTPRequestManager()
        self.threadManager = ProcessManager()
        self.settingsDialogController = SettingsExplorerDialogController()

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        pass

    # endregion

    # region - Configure
    def __configure(self):
        self.httpManager.onError.connect(self.__handleHttpManagerErrors)

    # endregion

    # region - Event Handlers
    @staticmethod
    def __handleHttpManagerErrors(message: str):
        signalBus.onLogErrorToOutput.emit(message)

    # endregion

    # region - Workers

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters

    # endregion

    # region - Setters

    # endregion
