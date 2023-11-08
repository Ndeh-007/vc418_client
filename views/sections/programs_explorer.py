from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGridLayout, QListView

from views.components.section_header import SectionHeader


class ProgramsExplorerView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # region header
        header = SectionHeader("Programs")
        layout.addWidget(header)

        # endregion

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

        layout.setVerticalSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)

        self.setLayout(layout)
        self.setObjectName("ProgramsExplorerView")
