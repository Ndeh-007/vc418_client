from PySide6.QtWidgets import QFrame, QVBoxLayout, QListView, QGraphicsView, QGraphicsScene


class TabPreviewCanvasView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.graphicsView = QGraphicsView()
        self.graphicsView.setFrameStyle(QFrame.Shape.NoFrame)
        self.scene = QGraphicsScene()

        layout.addWidget(self.graphicsView)
        self.setLayout(layout)
