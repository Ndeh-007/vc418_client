import qtawesome
from PySide6.QtWidgets import QFrame, QPushButton, QGridLayout, QTextEdit

from styles.color import appColors
from views.components.section_header import SectionHeader


class OutputExplorerView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # region - Header control buttons
        controlButtons = []

        self.clearBtn = QPushButton()
        ic = qtawesome.icon("msc.clear-all", color=appColors.dark_rbg)
        self.clearBtn.setIcon(ic)
        self.clearBtn.setFlat(True)

        self.minimizeBtn = QPushButton()
        ic = qtawesome.icon("msc.chrome-minimize", color=appColors.dark_rbg)
        self.minimizeBtn.setIcon(ic)
        self.minimizeBtn.setFlat(True)

        controlButtons.append(self.clearBtn)
        controlButtons.append(self.minimizeBtn)

        # endregion

        header = SectionHeader("Output", control_buttons=controlButtons)
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
