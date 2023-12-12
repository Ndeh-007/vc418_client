from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFrame, QVBoxLayout, QToolBar

from controllers.components.playback_widget_controller import PlayBackWidgetController


class TabControlToolbarView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = QToolBar()

        # define the actions
        # has a playback, fetch, build tree, clear canvas,
        self.reloadAction = QAction("Reload", self.toolbar)
        self.executeAction = QAction("Run", self.toolbar)

        self.playbackWidget = PlayBackWidgetController()

        # attach the actions to the toolbar
        self.toolbar.addAction(self.reloadAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.executeAction)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.playbackWidget)

        layout.addWidget(self.toolbar)
        self.setLayout(layout)

        self.setObjectName("TabControlToolbar")
