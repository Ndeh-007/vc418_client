from PySide6.QtCore import QLine
from PySide6.QtWidgets import QGraphicsLineItem, QGraphicsItem


class TreeLineItemController(QGraphicsLineItem):
    def __init__(self, line: QLine, parent: QGraphicsItem = None):
        super().__init__(line=line, parent=parent)
