import qtawesome

from styles.color import appColors
from views.components.status_bar import StatusBarView


class StatusBarController(StatusBarView):
    def __init__(self):
        super().__init__()

        eIcon = qtawesome.icon("fa5s.square", color=appColors.medium_rbg)
        self.erlangServerIndicator.setIcon(eIcon)
        self.erlangServerStatus.setText("offline")

        cppIcon = qtawesome.icon("fa5s.square", color=appColors.medium_rbg)
        self.cppServerIndicator.setIcon(cppIcon)
        self.cppServerStatus.setText("offline")

