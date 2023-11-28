import qtawesome

from interfaces.structs import MenuBarActionType, SystemRequestScope, ServerType, ServerState
from models.settings.server_model import ServerModel
from models.common.signal_data_models import SystemRequest, SystemRequestData, SystemAlert
from styles.color import appColors
from utils.signal_bus import signalBus
from views.components.status_bar import StatusBarView

import store.settings as ss


class StatusBarController(StatusBarView):
    def __init__(self):
        super().__init__()
        self.server: ServerModel = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        self.initialize()
        self.configure()

        self.__connectSignals()

    # region - Initialize
    def initialize(self):
        self.__updateServerStatusText(self.server)

    # endregion

    # region - configure

    def configure(self):
        self.erlangServerBtn.clicked.connect(self.__handelErlangServerButtonClicked)
        self.outputBtn.clicked.connect(self.__handleOutputButtonClicked)

    # endregion

    # region - Event Handlers
    def __handelErlangServerButtonClicked(self):

        if self.server.state() == ServerState.OFF:
            d = SystemRequestData(MenuBarActionType.START_SERVER, self.server.id())
            self.__fireSystemRequest(d)
            return

        if self.server.state() == ServerState.ON:
            d = SystemRequestData(MenuBarActionType.STOP_SERVER, self.server.id())
            self.__fireSystemRequest(d)
            return

    def __handleServerStateChanged(self, server: ServerModel):
        if server.id() == self.server.id():
            # update the local server value
            self.__updateServerStatusText(server)
            self.server = server

        else:
            alert = SystemAlert(f"Invalid server, expected: {self.server.serverType()}, got: {server.serverType()}")
            signalBus.onSystemAlert.emit(alert)

    def __handleOutputButtonClicked(self):
        d = SystemRequestData(MenuBarActionType.TOGGLE_OUTPUT_EXPLORER, MenuBarActionType.TOGGLE_OUTPUT_EXPLORER)
        self.__fireSystemRequest(d)

    # endregion

    # region - Workers
    def __updateServerStatusText(self, server: ServerModel):
        state = server.state()
        if state == ServerState.OFF:
            eIcon = qtawesome.icon("fa5s.square", color=appColors.medium_rbg)
            self.erlangServerIndicator.setIcon(eIcon)
            self.erlangServerStatus.setText("offline")
            self.erlangServerStatus.setStyleSheet(f"color:{appColors.medium_rbg};")
            return
        if state == ServerState.ON:
            eIcon = qtawesome.icon("fa5s.square", color=appColors.primary_rbg)
            self.erlangServerIndicator.setIcon(eIcon)
            self.erlangServerStatus.setText("online")
            self.erlangServerStatus.setStyleSheet(f"color:{appColors.primary_rbg};")
            return
        if state == ServerState.WORKING:
            eIcon = qtawesome.icon("fa5s.spinner", color=appColors.primary_rbg, animation=qtawesome.Spin(self.erlangServerIndicator))
            self.erlangServerIndicator.setIcon(eIcon)
            self.erlangServerStatus.setText("working")
            self.erlangServerStatus.setStyleSheet(f"color:{appColors.primary_rbg};")
            return
        if state == ServerState.TRANSITION:
            eIcon = qtawesome.icon("fa5s.spinner", color=appColors.medium_rbg, animation=qtawesome.Spin(self.erlangServerIndicator))
            self.erlangServerIndicator.setIcon(eIcon)
            self.erlangServerStatus.setText("transition")
            self.erlangServerStatus.setStyleSheet(f"color:{appColors.medium_rbg};")
            return

    @staticmethod
    def __fireSystemRequest(data: SystemRequestData, scope: SystemRequestScope = None):
        if scope:
            request = SystemRequest(data, scope)
        else:
            request = SystemRequest(data)
        signalBus.onSystemRequest.emit(request)

    # endregion

    # region connect signals
    def __connectSignals(self):
        signalBus.onServerStatusChanged.connect(self.__handleServerStateChanged)
    # endregion
