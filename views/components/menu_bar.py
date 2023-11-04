from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QFrame, QHBoxLayout


class MenuBarView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # define the layout
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # define the menubar
        self.menubar = QMenuBar()

        # define menubar actions
        fileAction = QAction("File", self)
        self.menubar.addAction(fileAction)

        layout.addWidget(self.menubar)
        layout.addStretch(1)

        self.setLayout(layout)
