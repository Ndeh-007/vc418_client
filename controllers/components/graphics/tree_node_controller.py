from PySide6.QtCore import QPointF, QRect
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsItem


class TreeNodeItemController(QGraphicsRectItem):
    """
    this item holds a node of the tree.
    """

    def __init__(self, parentNode=None, rect: QRect = None, parent: QGraphicsItem = None):
        super().__init__(rect=rect, parent=parent)

        self.__parentNode: TreeNodeItemController = parentNode
        self.__left: QPointF = QPointF(0, 0)
        self.__right: QPointF = QPointF(0, 0)
        self.__bottom: QPointF = QPointF(0, 0)
        self.__top: QPointF = QPointF(0, 0)

        self.__initAnchorsFromRect()

    # region override

    def setPos(self, pos) -> None:
        super().setPos(pos)
        self.__initAnchorsFromRect()

    def moveBy(self, dx: float, dy: float) -> None:
        super().moveBy(dx, dy)
        self.__initAnchorsFromRect()

    def setRect(self, rect):
        super().setRect(rect)
        self.__initAnchorsFromRect()

    # endregion

    # region workers

    def __initAnchorsFromRect(self):
        midY = (self.rect().top() + self.rect().bottom()) / 2
        midX = (self.rect().left() + self.rect().right()) / 2

        self.__left: QPointF = QPointF(self.rect().left(), midY)
        self.__right: QPointF = QPointF(self.rect().right(), midY)
        self.__bottom: QPointF = QPointF(midX, self.rect().bottom())
        self.__top: QPointF = QPointF(midX, self.rect().top())

    # endregion

    # region getters

    def top(self):
        return self.__top

    def bottom(self):
        return self.__bottom

    def left(self):
        return self.__left

    def right(self):
        return self.__right

    def anchors(self):
        return [
            self.__left,
            self.__right,
            self.__bottom,
            self.__top
        ]

    # endregion

    # region setters

    def setTop(self, point: QPointF):
        self.__top = point

    def setBottom(self, point: QPointF):
        self.__bottom = point

    def setRight(self, point: QPointF):
        self.__right = point

    def setLeft(self, point: QPointF):
        self.__left = point

    def setAnchors(self, points: list[QPointF]):
        self.__top: QPointF = points[0]
        self.__right: QPointF = points[1]
        self.__bottom: QPointF = points[2]
        self.__left: QPointF = points[3]

    # endregion
