from PySide6.QtCore import QRect
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsItem

from models.graphics.tree_node_model import TreeNodeModel


class TreeNodeItemController(QGraphicsRectItem):
    """
    this item holds a node of the tree. configurations for click and user interactions happens here.
    """

    def __init__(self, processID: str, parentNode: TreeNodeModel = None, rect: QRect = None,
                 parent: QGraphicsItem = None, model: TreeNodeModel = None):
        """

        :param processID: the process the node belongs to
        :param parentNode: the parent of this node if any exist
        :param rect: rectangle to be drawn on the canvas
        :param parent: the graphics item that holds this item
        """
        super().__init__()

        self.__parentNode: TreeNodeModel = parentNode

        if model is None:
            self.__node: TreeNodeModel = TreeNodeModel(processID)
        else:
            self.__node: TreeNodeModel = model

        if rect is not None:
            self.setRect(rect)

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
        self.__node.resetAnchors(self.rect())

    # endregion

    # region getters

    def node(self):
        return self.__node

    def parentNode(self):
        return self.__parentNode

    # endregion

    # region setters

    def setNode(self, node: TreeNodeModel):
        self.__node = node

    def setParentNode(self, node: TreeNodeModel | None):
        self.__parentNode = node

    # endregion
