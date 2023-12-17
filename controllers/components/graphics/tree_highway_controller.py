from typing import Literal

from PySide6.QtCore import QRect, QPointF, QLine
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsLineItem

from models.graphics.tree_highway_model import TreeHighwayModel


class TreeHighwayController(QGraphicsLineItem):
    def __init__(self, model: TreeHighwayModel):
        super().__init__()
        self.__highwayModel: TreeHighwayModel = model
        self.__rectPadding: int = 1

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

    # region private workers
    def __computeBoundingRect(self) -> QRect:
        """
        taking into account the height of arrow (highway direction) and the average height for the text (highway value)
        a rectangle is calculated and estimated to hold these values with a rectangle padding of `self.__rectPadding`.

        the left and right anchor points of the model are used as the top-left and bottom-right points of the rectangle
        without the paddings (arrowHeight + textHeight + highwayThickness)
        :return:
        """

        if self.__highwayModel.direction() == "left":
            topLeft = QPointF(
                self.__highwayModel.toAnchor().x() - self.__computeOffsetDistance("horizontal"),
                self.__highwayModel.toAnchor().y() - self.__computeOffsetDistance('vertical')
            ).toPoint()
            bottomRight = QPointF(
                self.__highwayModel.fromAnchor().x() + self.__computeOffsetDistance("horizontal"),
                self.__highwayModel.fromAnchor().y() + self.__computeOffsetDistance('vertical')
            ).toPoint()
            return QRect(topLeft, bottomRight)
        elif self.__highwayModel.direction() == "right":
            topLeft = QPointF(
                self.__highwayModel.fromAnchor().x() - self.__computeOffsetDistance("horizontal"),
                self.__highwayModel.fromAnchor().y() - self.__computeOffsetDistance('vertical')
            ).toPoint()
            bottomRight = QPointF(
                self.__highwayModel.toAnchor().x() + self.__computeOffsetDistance("horizontal"),
                self.__highwayModel.toAnchor().y() + self.__computeOffsetDistance('vertical')
            ).toPoint()
            return QRect(topLeft, bottomRight)
        else:
            # no arrows, we return an empty line accounting only for thickness.
            # in this case, the direction of the offset does not matter
            return QRect(
                QPointF(
                    self.__highwayModel.fromAnchor().x() - self.__rectPadding,
                    self.__highwayModel.fromAnchor().y() - self.__highwayModel.thickness() / 2 - self.__rectPadding
                ).toPoint(),
                QPointF(
                    self.__highwayModel.toAnchor().x() + self.__rectPadding,
                    self.__highwayModel.toAnchor().y() + self.__highwayModel.thickness() / 2 + self.__rectPadding
                ).toPoint(),
            )

    def __computeOffsetDistance(self, plane: Literal['horizontal', 'vertical']):
        if plane == 'horizontal':
            offset = self.__rectPadding + self.__highwayModel.thickness() + self.__highwayModel.rightArrow().width()
            return offset
        if plane == 'vertical':
            offset = self.__rectPadding + self.__highwayModel.thickness() + self.__highwayModel.rightArrow().height()
            return offset

    # endregion

    # region - public workers
    def reset(self):
        """
        resets the values of the model to original empty values. such that nothing will be painted for this particular
        model.
        changes the model.__direction=none, sets model.__data=none or an empty string.
        we preserve the anchor points and all other information
        :return:
        """
        self.__highwayModel.setData(None)
        self.__highwayModel.setArrowDirection(None)
    # endregion

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters
    def model(self):
        return self.__highwayModel

    # endregion

    # region - Setters
    def updateTraffic(self, model: TreeHighwayModel):
        """
        here we handle changes in the current arrow being rendered whether it is left or right and we also update
        the data that is being rendered. it updates all fields except the left and right arrows
        :param model:
        :return:
        """
        self.__highwayModel.setData(model.data())
        self.__highwayModel.setArrow(model.arrow())
        self.__highwayModel.setToPid(model.toPid())
        self.__highwayModel.setFromPid(model.fromPid())
        self.__highwayModel.setToAnchor(model.toAnchor())
        self.__highwayModel.setFromAnchor(model.fromAnchor())
        self.__highwayModel.setThickness(model.thickness())
        self.__highwayModel.setArrowDirection(model.direction())

    def setTrafficDirection(self, direction: Literal["left", "right"] | None):
        """

        :param direction:
        :return:
        """
        self.__highwayModel.setArrowDirection(direction)

    def setTrafficValue(self, value: str):
        """
        changes the value on the highway
        :param value:
        :return:
        """
        self.__highwayModel.setData(value)

    def setModel(self, model: TreeHighwayModel):
        self.__highwayModel = model

    # endregion

    # region - Override
    def boundingRect(self):
        return self.__computeBoundingRect()

    def paint(self, painter: QPainter, option, widget=...):
        super().paint(painter, option, widget)

        """
        regardless of the arrow direction, user the center point of the line in correlation with the line thickness
        to draw the arrow and write the text.
        
        the bottom right of the arrow should be on the center point of the line (accounting for the line thickness)
        the top-left of the text box should be on the bottom of the line starting from the center point.
        
        if no direction if is in-play we draw only the line with no text. 
        """
        direction = self.__highwayModel.direction()
        center = self.__highwayModel.midPoint()

        # first draw the line
        painter.drawLine(
            QLine(
                self.__highwayModel.fromAnchor().toPoint(),
                self.__highwayModel.toAnchor().toPoint()
            )
        )
        if direction is not None:
            # paint the left arrow
            # compute the offset of the point from the center
            topLeft = QPointF(
                center.x() - self.__highwayModel.arrow().width(),
                center.y() - self.__highwayModel.arrow().height(),
            ).toPoint()
            painter.drawPixmap(topLeft, self.__highwayModel.arrow())
            # write the text
            painter.drawText(center, self.__highwayModel.data())

        # if direction == 'right':
        #     # paint the right arrow
        #     # compute the offset of the point from the center
        #     topLeft = QPointF(
        #         center.x() - self.__highwayModel.rightArrow().width(),
        #         center.y() - self.__highwayModel.rightArrow().height(),
        #     ).toPoint()
        #     painter.drawPixmap(topLeft, self.__highwayModel.rightArrow())
        #     # write the text
        #     painter.drawText(center.toPoint(), self.__highwayModel.data())

    # endregion
