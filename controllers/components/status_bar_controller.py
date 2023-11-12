import qtawesome

from styles.color import appColors
from utils.signal_bus import signalBus
from views.components.status_bar import StatusBarView


class StatusBarController(StatusBarView):
    def __init__(self):
        super().__init__()
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

    # endregion

    # region - Event Handlers
    def __handelErlangServerButtonClicked(self):
        signalBus.onLogToOutput.emit("Server BTn clicked")
    # endregion
