from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGridLayout, QLabel

from views.components.section_header import SectionHeader


class OutputExplorerView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        header = SectionHeader("Output")
        layout.addWidget(header)

        tallBtn = QPushButton("SectionBody")
        layout.addWidget(tallBtn)

        layout.setVerticalSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 0)

        self.setLayout(layout)
        self.setObjectName("OutputExplorerView")

        # self.setMaximumHeight(100)
