import uuid

from PySide6 import QtGui
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel

from controllers.components.tab_control_toolbar_controller import TabControlToolbarController


class ProgramPreviewItemView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        controlBar = TabControlToolbarController()
        layout.addWidget(controlBar)

        layout.addStretch()

        self.setLayout(layout)
