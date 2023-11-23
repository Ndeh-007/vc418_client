from PySide6.QtWidgets import QFrame, QVBoxLayout, QListView


class TabPreviewCanvasView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QListView())
        self.setLayout(layout)
