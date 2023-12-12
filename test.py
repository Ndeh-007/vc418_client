from PySide6.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView, QMainWindow, QWidget
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter, QPen, QColor
import sys

class ArrowItem(QGraphicsItem):
    def __init__(self):
        super().__init__()

        # Set the bounding rectangle for the arrow
        self.rect = QRectF(0, 0, 100, 50)

    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing)

        # Define the points for drawing the arrow
        points = [
            self.rect.topLeft(),             # Start at top left corner
            self.rect.topRight(),            # Move to top right corner
            self.rect.bottomRight(),         # Move to bottom right corner
            self.rect.center(),              # Move to center bottom
            self.rect.bottomLeft(),          # Move to bottom left corner
            self.rect.topLeft()              # Move back to top left corner (closing the arrow)
        ]

        # Create a pen for drawing the arrow outline
        pen = QPen()
        pen.setColor(QColor("black"))
        pen.setWidth(2)
        painter.setPen(pen)

        # Draw the arrow using the calculated points
        painter.drawPolyline(points)

def main():
    app = QApplication(sys.argv)

    scene = QGraphicsScene()
    view = QGraphicsView(scene)

    arrow_item = ArrowItem()
    scene.addItem(arrow_item)

    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
