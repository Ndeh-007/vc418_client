from PySide6.QtWidgets import QFrame, QVBoxLayout

from controllers.components.tab_control_toolbar_controller import TabControlToolbarController
from controllers.components.tab_preview_canvas_controller import TabPreviewCanvasController


class ProgramPreviewItemView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.controlBar = TabControlToolbarController()
        layout.addWidget(self.controlBar)

        self.canvas = TabPreviewCanvasController()

        layout.addWidget(self.canvas)

        self.setLayout(layout)
