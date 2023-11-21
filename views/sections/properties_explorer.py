import qtawesome
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGridLayout, QListView, QScrollArea, QLabel, QLineEdit, \
    QStackedLayout

from styles.color import appColors
from utils.styling import setPaletteColor
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

        # controlButtons.append(self.minimizeBtn)

        # endregion

        header = SectionHeader("Properties", control_buttons=controlButtons)
        layout.addWidget(header)
        # endregion

        # region content holder

        contentHolder = QFrame()
        self.contentLayout = QStackedLayout()
        self.contentLayout.setContentsMargins(0, 0, 0, 0)

        # region body
        body = QFrame()
        bodyLayout = QVBoxLayout()
        bodyLayout.setContentsMargins(0, 0, 0, 0)

        bodyContentHolder = QFrame()
        bodyContentHolderLayout = QVBoxLayout()
        bodyContentHolderLayout.setContentsMargins(0, 0, 0, 0)

        # region body content
        bodyContent = QFrame()
        bodyContentLayout = QGridLayout()

        # define the title
        self.programTitleLabel = QLabel()
        self.programTitleLabel.setObjectName("PreviewExplorerPlaceholderLabel")
        bodyContentLayout.addWidget(self.programTitleLabel, 0, 0, 1, 2)

        # define n procs input
        nProcsLabel = QLabel("Processes")
        self.nProcsInput = QLineEdit()
        bodyContentLayout.addWidget(nProcsLabel, 1, 0)
        bodyContentLayout.addWidget(self.nProcsInput, 1, 1)

        bodyContent.setLayout(bodyContentLayout)
        # endregion

        bodyContentHolderLayout.addWidget(bodyContent)
        bodyContentHolderLayout.addStretch()

        bodyContentHolder.setLayout(bodyContentLayout)

        setPaletteColor(body, appColors.white)

        bodyLayout.addWidget(bodyContentHolder)
        bodyLayout.addStretch()
        body.setLayout(bodyLayout)

        self.contentLayout.addWidget(body)
        # endregion

        # region content placeholder
        placeholder = QFrame()
        placeholderLayout = QVBoxLayout()
        placeholderLayout.setContentsMargins(0, 0, 0, 0)
        placeholderLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        placeHolderText = QLabel("No Program Selected")
        placeHolderText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeHolderText.setWordWrap(True)
        placeHolderText.setObjectName("PreviewExplorerPlaceholderLabelValue")
        placeholderLayout.addWidget(placeHolderText)

        placeholder.setLayout(placeholderLayout)
        self.contentLayout.addWidget(placeholder)

        contentHolder.setLayout(self.contentLayout)
        # endregion

        layout.addWidget(contentHolder)

        # endregion

        layout.setVerticalSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)

        self.setLayout(layout)
        self.setObjectName("PropertiesExplorerView")
