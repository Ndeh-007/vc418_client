import uuid

from PySide6 import QtGui
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel


class ProgramPreviewItemView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel(str(uuid.uuid4())))

        self.setLayout(layout)

