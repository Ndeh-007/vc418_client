from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel


class HomePage(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel("aksujda"))

        self.setLayout(layout)
