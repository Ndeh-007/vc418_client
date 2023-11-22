from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFrame, QVBoxLayout, QToolBar


class TabControlToolbarView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = QToolBar()

        # define the actions
        # has a playback, fetch, build tree, clear canvas,
        self.fetchAction = QAction("Fetch", self.toolbar)
        self.executeAction = QAction("Execute", self.toolbar)

        # attach the actions to the toolbar
        self.toolbar.addAction(self.fetchAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.executeAction)
        self.toolbar.addSeparator()

        layout.addWidget(self.toolbar)
        self.setLayout(layout)

        self.setObjectName("TabControlToolbar")

