from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QFrame, QHBoxLayout


class MenuBarView(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # define menubar actions
        fileAction = QAction("File", self)
        self.addAction(fileAction)

