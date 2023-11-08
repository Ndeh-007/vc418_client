from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGridLayout, QLabel, QTextEdit

from views.components.section_header import SectionHeader


class OutputExplorerView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        header = SectionHeader("Output")
        layout.addWidget(header)

        self.logger = QTextEdit()
        self.logger.setReadOnly(True)
        self.logger.setFrameStyle(QFrame.Shape.NoFrame)
        self.logger.setObjectName("outputTextArea")
        layout.addWidget(self.logger)

        layout.setVerticalSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 0)

        self.setLayout(layout)
        self.setObjectName("OutputExplorerView")
