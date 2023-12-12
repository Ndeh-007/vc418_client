from uuid import uuid4

from PySide6.QtCore import QPointF, QRect


class TreeNodeModel:
    def __init__(self, processID: str, socket: int = 0, level: int = 0, parentNode=None):

        self.__nodeID = str(uuid4())

        self.__parentNode: TreeNodeModel = parentNode

        self.__processID: str = processID

        self.__socket: int = socket
        self.__level: int = level

        self.__horizontalOffsetFactor: float = 60.0
        self.__verticalOffsetFactor: float = 60.0

        self.__left: QPointF = QPointF(0, 0)
        self.__right: QPointF = QPointF(0, 0)
        self.__bottom: QPointF = QPointF(0, 0)
        self.__top: QPointF = QPointF(0, 0)

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        pass

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    # endregion

    # region - Workers

    def incrementSocket(self, step: int = 1):
        """
        increments the sockets value by step
        :param step:
        :return:
        """
        self.__socket += step

    def resetAnchors(self, rect: QRect):
        """
        resets the anchor values to the center points of the provided rectangle.
        :param rect:
        :return:
        """
        midY = (rect.top() + rect.bottom()) / 2
        midX = (rect.left() + rect.right()) / 2

        self.__left: QPointF = QPointF(rect.left(), midY)
        self.__right: QPointF = QPointF(rect.right(), midY)
        self.__bottom: QPointF = QPointF(midX, rect.bottom())
        self.__top: QPointF = QPointF(midX, rect.top())
    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region getters
    def processID(self):
        return self.__processID

    def hOffsetFactor(self):
        return self.__horizontalOffsetFactor

    def vOffsetFactor(self):
        return self.__verticalOffsetFactor

    def level(self):
        return self.__level

    def socket(self):
        return self.__socket

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

    def nodeID(self):
        return self.__nodeID

    def parentNode(self):
        return self.__parentNode

    # endregion

    # region setters

    def setParentNode(self, node):
        self.__parentNode = node

    def setSocket(self, value: int):
        self.__socket = value

    def setLevel(self, value: int):
        self.__level = value

    def setVOffsetFactor(self, value: float):
        self.__verticalOffsetFactor = value

    def setHOffsetFactor(self, value: float):
        self.__horizontalOffsetFactor = value

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
