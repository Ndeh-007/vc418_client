from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGridLayout

from views.components.section_header import SectionHeader


class ProgramsExplorerView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        header = SectionHeader("Programs")
        layout.addWidget(header)

        layout.addWidget(QPushButton("SectionBody"))

        layout.setVerticalSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)

        self.setLayout(layout)
        self.setObjectName("ProgramsExplorerView")
