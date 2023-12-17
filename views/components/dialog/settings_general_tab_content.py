from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


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
        self.selectOutputFileButton = QPushButton("Browse ...")
        w2Layout.addWidget(l3)
        w2Layout.addWidget(self.outputFile)
        w2Layout.addWidget(self.selectOutputFileButton)
        w2Layout.addStretch()

        w2.setLayout(w2Layout)
        layout.addWidget(w2)

        # def option 2
        w3 = QFrame()
        w3Layout = QHBoxLayout()
        w3Layout.setContentsMargins(0, 0, 0, 0)

        l3 = QLabel('Server Path')
        self.serverPathInput = QLineEdit()
        self.selectServerPathButton = QPushButton("Browse ...")
        w3Layout.addWidget(l3)
        w3Layout.addWidget(self.serverPathInput)
        w3Layout.addWidget(self.selectServerPathButton)
        w3Layout.addStretch()

        w3.setLayout(w3Layout)
        layout.addWidget(w3)

        layout.addStretch()

        self.setLayout(layout)
