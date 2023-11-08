from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class PreviewExplorerPlaceholder(QFrame):
    def __init__(self):
        super(PreviewExplorerPlaceholder, self).__init__()

        # define ui
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap = QPixmap(":resources/images/burnt_logo.png")
        image = QLabel()
        image.setPixmap(pixmap.scaled(64, 64))

        label = QLabel("Welcome")
        value = QLabel("Open Projects, Launch Servers, Enjoy.")

        image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label.setObjectName("PreviewExplorerPlaceholderLabel")
        value.setObjectName("PreviewExplorerPlaceholderLabelValue")

        layout.addWidget(image)
        layout.addWidget(label)
        layout.addWidget(value)
        self.setLayout(layout)

        self.setFrameStyle(QFrame.Shape.NoFrame)

        self.setObjectName("PreviewExplorerPlaceholder")

