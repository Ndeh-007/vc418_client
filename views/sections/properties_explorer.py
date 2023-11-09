import qtawesome
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGridLayout, QListView

from styles.color import appColors
from views.components.section_header import SectionHeader


class PropertyExplorerView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # region header

        # region - Header control buttons
        controlButtons = []

        self.minimizeBtn = QPushButton()
        ic = qtawesome.icon("msc.chrome-minimize", color=appColors.dark_rbg)
        self.minimizeBtn.setIcon(ic)
        self.minimizeBtn.setFlat(True)

        controlButtons.append(self.minimizeBtn)

        # endregion

        header = SectionHeader("Properties", control_buttons=controlButtons)
        layout.addWidget(header)
        # endregion

        # region body

        # region body
        body = QFrame()
        bodyLayout = QVBoxLayout()
        bodyLayout.setContentsMargins(0, 0, 0, 0)

        self.programsListView = QListView()
        self.programsListView.setFrameStyle(QFrame.Shape.NoFrame)
        bodyLayout.addWidget(self.programsListView)

        body.setLayout(bodyLayout)

        layout.addWidget(body)
        # endregion

        # endregion

        layout.setVerticalSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)

        self.setLayout(layout)
        self.setObjectName("PropertiesExplorerView")

