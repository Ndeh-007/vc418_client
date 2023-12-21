import qtawesome
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, \
    QStackedLayout, QHBoxLayout, QTableView, QComboBox

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
        bodyContentLayout = QVBoxLayout()
        # bodyContentLayout.setContentsMargins(0, 0, 0, 0)

        # # define the title
        self.programTitleLabel = QLabel()
        self.programTitleLabel.setObjectName("PreviewExplorerPlaceholderLabel")
        bodyContentLayout.addWidget(self.programTitleLabel)

        # # define n procs
        w0 = QFrame()
        w0Layout = QHBoxLayout()
        w0Layout.setContentsMargins(0, 0, 0, 0)

        # define n procs input
        nProcsLabel = QLabel("Processes")
        self.nProcsInput = QLineEdit()
        w0Layout.addWidget(nProcsLabel)
        w0Layout.addStretch()
        w0Layout.addWidget(self.nProcsInput)

        w0.setLayout(w0Layout)
        bodyContentLayout.addWidget(w0)

        # define frames preview section
        # define frames preview summary
        w = QFrame()
        wLayout = QHBoxLayout()
        wLayout.setContentsMargins(0, 0, 0, 0)

        l1 = QLabel("Frames: ")
        l2 = QLabel("Current Frame:")
        self.totalFramesLabel = QLabel()
        self.currentFrameLabel = QLabel()

        wLayout.addWidget(l1)
        wLayout.addWidget(self.totalFramesLabel)
        wLayout.addStretch()
        wLayout.addWidget(l2)
        wLayout.addWidget(self.currentFrameLabel)

        w.setLayout(wLayout)
        bodyContentLayout.addWidget(w)

        # define frame preview
        self.executionFramePreviewTabel = QTableView()
        self.executionFramePreviewTabel.setFrameShape(QFrame.Shape.NoFrame)
        bodyContentLayout.addWidget(self.executionFramePreviewTabel)

        # # define frame complete summary section
        # define header
        h = QFrame()
        hLayout = QHBoxLayout()
        hLayout.setContentsMargins(0, 0, 0, 0)

        l3 = QLabel("Process: ")
        self.currentPidLabel = QLabel()
        l4 = QLabel("Select: ")
        self.currentPidSelectionInput = QComboBox()

        hLayout.addWidget(l3)
        hLayout.addWidget(self.currentPidLabel)
        hLayout.addStretch()
        hLayout.addWidget(l4)
        hLayout.addWidget(self.currentPidSelectionInput)

        hLayout.setStretch(4, 2)
        h.setLayout(hLayout)
        bodyContentLayout.addWidget(h)

        # define frame complete summary
        self.pidExecutionTimelineTable = QTableView()
        self.pidExecutionTimelineTable.setFrameShape(QFrame.Shape.NoFrame)
        bodyContentLayout.addWidget(self.pidExecutionTimelineTable)

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
