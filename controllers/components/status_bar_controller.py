import qtawesome

from interfaces.structs import MenuBarActionType, SystemRequestScope
from models.signal_data_models import SystemRequest, SystemRequestData
from styles.color import appColors
from utils.signal_bus import signalBus
from views.components.status_bar import StatusBarView


class StatusBarController(StatusBarView):
    def __init__(self):
        super().__init__()
        self.serverState = False
        self.initialize()
        self.configure()

    # region - Initialize
    def initialize(self):
        eIcon = qtawesome.icon("fa5s.square", color=appColors.medium_rbg)
        self.erlangServerIndicator.setIcon(eIcon)
        self.erlangServerStatus.setText("offline")

    # endregion

    # region - configure

    def configure(self):
        self.erlangServerBtn.clicked.connect(self.__handelErlangServerButtonClicked)
        self.outputBtn.clicked.connect(self.__handleOutputButtonClicked)

    # endregion

    # region - Event Handlers
    def __handelErlangServerButtonClicked(self):
        if not self.serverState:
            d = SystemRequestData(MenuBarActionType.START_SERVER, None)
        else:
            d = SystemRequestData(MenuBarActionType.STOP_SERVER, None)
        self.serverState = not self.serverState
        self.__fireSystemRequest(d)

    def __handleOutputButtonClicked(self):
        d = SystemRequestData(MenuBarActionType.TOGGLE_OUTPUT_EXPLORER, MenuBarActionType.TOGGLE_OUTPUT_EXPLORER)
        self.__fireSystemRequest(d)

    # endregion

    # region - Workers
    @staticmethod
    def __fireSystemRequest(data: SystemRequestData, scope: SystemRequestScope = None):
        if scope:
            request = SystemRequest(data, scope)
        else:
            request = SystemRequest(data)
        signalBus.onSystemRequest.emit(request)

    # endregion