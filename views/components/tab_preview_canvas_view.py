from PySide6.QtWidgets import QFrame, QGraphicsView, QGraphicsScene


class TabPreviewCanvasView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.NoFrame)
        self.scene = QGraphicsScene()

        self.setScene(self.scene)