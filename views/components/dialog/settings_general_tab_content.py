import qtawesome
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout, QComboBox

from styles.color import appColors


class SettingsGeneralTabContentView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # def option 1
        w1 = QFrame()
        w1Layout = QHBoxLayout()
        w1Layout.setContentsMargins(0, 0, 0, 0)

        l1 = QLabel('Framerate')
        self.frameRateInput = QLineEdit()
        l2 = QLabel('fps')
        w1Layout.addWidget(l1)
        w1Layout.addWidget(self.frameRateInput)
        w1Layout.addWidget(l2)
        w1Layout.addStretch()

        w1.setLayout(w1Layout)
        layout.addWidget(w1)

        # def option 2
        w2 = QFrame()
        w2Layout = QHBoxLayout()
        w2Layout.setContentsMargins(0, 0, 0, 0)

        l3 = QLabel('Output File')
        self.outputFile = QLineEdit()
        self.selectOutputFileButton = QPushButton()
        ic = qtawesome.icon("msc.go-to-file", color=appColors.medium_tint_rbg)
        self.selectOutputFileButton.setIcon(ic)
        w2Layout.addWidget(l3)
        w2Layout.addWidget(self.outputFile)
        w2Layout.addWidget(self.selectOutputFileButton)
        w2Layout.addStretch()

        w2.setLayout(w2Layout)
        layout.addWidget(w2)

        # def option 3
        w3 = QFrame()
        w3Layout = QHBoxLayout()
        w3Layout.setContentsMargins(0, 0, 0, 0)

        l3 = QLabel('Server Path')
        self.serverPathInput = QLineEdit()
        self.selectServerPathButton = QPushButton()
        ic = qtawesome.icon("msc.folder", color=appColors.medium_tint_rbg)
        self.selectServerPathButton.setIcon(ic)
        w3Layout.addWidget(l3)
        w3Layout.addWidget(self.serverPathInput)
        w3Layout.addWidget(self.selectServerPathButton)
        w3Layout.addStretch()

        w3.setLayout(w3Layout)
        layout.addWidget(w3)

        # def option 4
        w4 = QFrame()
        w4Layout = QHBoxLayout()
        w4Layout.setContentsMargins(0, 0, 0, 0)

        l4 = QLabel('Rebar Location')
        self.rebarLocation = QLineEdit()
        self.selectRebarFileButton = QPushButton()
        ic = qtawesome.icon("msc.go-to-file", color=appColors.medium_tint_rbg)
        self.selectRebarFileButton.setIcon(ic)
        w4Layout.addWidget(l4)
        w4Layout.addWidget(self.rebarLocation)
        w4Layout.addWidget(self.selectRebarFileButton)
        w4Layout.addStretch()

        w4.setLayout(w4Layout)
        layout.addWidget(w4)

        # def option 5
        w4 = QFrame()
        w4Layout = QGridLayout()
        w4Layout.setContentsMargins(0, 0, 0, 0)

        l4_1 = QLabel('Protocol')
        self.protocolSelectionComboBox = QComboBox()
        w4Layout.addWidget(l4_1, 0,0)
        w4Layout.addWidget(self.protocolSelectionComboBox,0,1)

        l4_2 = QLabel('Domain')
        self.domainInput = QLineEdit()
        w4Layout.addWidget(l4_2, 0,2)
        w4Layout.addWidget(self.domainInput,0,3)

        l4_3 = QLabel('Port')
        self.portNumberInput = QLineEdit()
        w4Layout.addWidget(l4_3, 1,0)
        w4Layout.addWidget(self.portNumberInput,1,1)

        # l4_1 = QLabel('Domain')
        # self.domainSelectionComboBox = QComboBox()
        # w4Layout.addWidget(l4_1, 1,2)
        # w4Layout.addWidget(self.domainSelectionComboBox,1,3)

        w4.setLayout(w4Layout)
        layout.addWidget(w4)

        layout.addStretch()

        self.setLayout(layout)
