from PySide6.QtWidgets import QFrame, QVBoxLayout, QToolBar


class TabControlToolbarView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = QToolBar()

        # define the actions

        # attach the actions to the toolbar

        layout.addWidget(self.toolbar)
        self.setLayout(layout)

        self.setObjectName("TabControlToolbar")
