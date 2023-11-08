from PySide6.QtWidgets import QFrame, QProgressBar, QHBoxLayout


class LoadingBarView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.progressBar = QProgressBar()

        layout.addWidget(self.progressBar)
        self.setLayout(layout)
