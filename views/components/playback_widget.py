import qtawesome
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QLineEdit


class PlayBackView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("Playback")
        layout.addWidget(title)

        self.previousBtn = QPushButton()
        self.previousBtn.setFlat(True)
        ic = qtawesome.icon("fa5s.step-backward")
        self.previousBtn.setIcon(ic)

        self.nextBtn = QPushButton()
        self.nextBtn.setFlat(True)
        ic = qtawesome.icon("fa5s.step-forward")
        self.nextBtn.setIcon(ic)

        self.playPauseBtn = QPushButton()
        self.playPauseBtn.setFlat(True)
        ic = qtawesome.icon("fa5s.play")
        self.playPauseBtn.setIcon(ic)

        framesLabel = QLabel("frame")
        self.framesInput = QLineEdit()
        self.framesInput.setObjectName("framesInput")
        self.framesInput.setMaximumWidth(50)
        self.framesTotal = QLabel()

        layout.addWidget(self.previousBtn)
        layout.addWidget(self.playPauseBtn)
        layout.addWidget(self.nextBtn)
        layout.addWidget(framesLabel)
        layout.addWidget(self.framesInput)
        layout.addWidget(self.framesTotal)

        layout.addStretch()

        self.setLayout(layout)