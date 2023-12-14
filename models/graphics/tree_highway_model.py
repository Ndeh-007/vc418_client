import uuid
from typing import Literal

from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QPixmap


class TreeHighwayModel:
    def __init__(self,
                 fromAnchor: QPoint | QPointF = None,
                 toAnchor: QPoint | QPointF = None,
                 fromPid: str = None,
                 toPid: str = None,
                 data: str = None,
                 leftArrow: QPixmap = None,
                 rightArrow: QPixmap = None,
                 thickness: int = 1
                 ):
        self.__fromAnchor: QPoint | QPointF = fromAnchor
        self.__toAnchor: QPoint | QPointF = toAnchor
        self.__fromPid: str = fromPid
        self.__toPid: str = toPid
        self.__data: str = data
        self.__leftArrow: QPixmap = leftArrow
        self.__rightArrow: QPixmap = rightArrow
        self.__arrow: QPixmap | None = leftArrow  # by default the main direction is left
        self.__direction: Literal["left", "right"] | None = "left" if leftArrow is not None else None
        self.__thickness: int = thickness
        self.__id: str = str(uuid.uuid4())

    # region - Getters

    def id(self):
        return self.__id

    def direction(self):
        return self.__direction

    def thickness(self):
        return self.__thickness

    def midPoint(self):
        return self.__computeAnchorsMidPoint()

    def arrow(self):
        return self.__arrow

    def fromAnchor(self):
        return self.__fromAnchor

    def toAnchor(self):
        return self.__toAnchor

    def fromPid(self):
        return self.__fromPid

    def toPid(self):
        return self.__toPid

    def data(self):
        return self.__data

    def leftArrow(self):
        return self.__leftArrow

    def rightArrow(self):
        return self.__rightArrow

    # endregion

    # region - Setters

    def setThickness(self, value: int):
        self.__thickness = value

    def setFromAnchor(self, value: QPointF | QPoint):
        self.__fromAnchor = value

    def setToAnchor(self, value: QPointF | QPoint):
        self.__toAnchor = value

    def setFromPid(self, value: str):
        self.__fromPid = value

    def setToPid(self, value: str):
        self.__toPid = value

    def setData(self, value: str | None):
        self.__data = value

    def setRightArrow(self, arrow: QPixmap):
        self.__rightArrow = arrow

    def setLeftArrow(self, arrow: QPixmap):
        self.__leftArrow = arrow

    def setArrow(self, arrow: QPixmap):
        self.__arrow = arrow

    def setArrowDirection(self, direction: Literal["left", "right"] | None):
        if direction == 'left':
            self.__arrow = self.__leftArrow
            self.__direction = direction
            return

        if direction == "right":
            self.__arrow = self.__rightArrow
            self.__direction = direction
            return

        if direction is None:
            self.__direction = direction
            return

    # endregion

    # region - Workers

    def __computeAnchorsMidPoint(self):
        return QPointF(
            (self.__fromAnchor.x() + self.__toAnchor.x())/2,
            (self.__fromAnchor.y() + self.__toAnchor.y())/2
        )
    # endregion
