from PySide6.QtWidgets import QFrame, QVBoxLayout, QWidget


class TabContentHolder(QFrame):
    def __init__(self, content: QWidget):
        super().__init__()

        self.content = content

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.content)

        self.setLayout(layout)
