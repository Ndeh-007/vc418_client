from PySide6.QtWidgets import QFrame, QVBoxLayout, QTabWidget


class SettingsExplorerView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.settingsTabWidget = QTabWidget()
        layout.addWidget(self.settingsTabWidget)

        self.setLayout(layout)
