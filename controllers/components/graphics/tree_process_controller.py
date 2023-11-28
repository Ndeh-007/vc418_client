from PySide6.QtCore import QRect, QPoint, QSize
from PySide6.QtWidgets import QGraphicsItem

from controllers.components.graphics.tree_node_controller import TreeNodeItemController
from models.graphics.tree_process_model import TreeProcessModel


class TreeProcessItemController(QGraphicsItem):
    """
    This graphics item handles a single process.
    each process has its nodes and connectors
    """

    def __init__(self, processModel: TreeProcessModel = None):
        super().__init__()

        self.__processModel: TreeProcessModel = processModel
        self.__nodes: list[TreeNodeItemController] = []

        self.__baseRect = QRect(QPoint(0, 0), QSize(10, 10))

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

    def __createNodes(self):
        """
        creates controller nodes based on the models provided
        :return:
        """
        cNodes = []
        nodes = self.__processModel.nodes()

        # first create the first node
        n = TreeNodeItemController(processID=self.__processModel.processID(), parentNode=None, rect=self.__baseRect,
                                   parent=self)
        cNodes.append(n)

        # check if the there is only one node to be created
        if len(nodes) == 1:
            return

            # create the rest of the nodes otherwise
        for i in range(1, len(nodes)):
            vShift = i * nodes[i].vOffsetFactor()
            n = TreeNodeItemController(processID=self.__processModel.processID(),
                                       parentNode=None,
                                       rect=QRect(QPoint(self.__baseRect.left(), vShift + self.__baseRect.bottom()),
                                                  self.__baseRect.size()),
                                       parent=self)
            cNodes.append(n)

        self.__nodes = cNodes

    def connectNodes(self):
        """
        connects the nodes for this process, such that each node has its parent as the one that came before it.
        the first node does not have a parent.
        :return:
        """
        # set the parent of the first node to None
        self.__nodes[0].setParentNode(None)
        _l = len(self.__nodes)

        # check the length of the nodes
        if _l == 1:
            return

        # attach the nodes to the one that came before it
        for i in range(1, _l):
            self.__nodes[i].setParentNode(self.__nodes[i - 1].node())

    # endregion

    # region - Connect Signals

    def __connectSignals(self):

        pass

    # endregion

    # region - Getters
    def processModel(self):
        return self.__processModel

    # endregion

    # region - Setters
    def setProcessModel(self, processModel: TreeProcessModel):
        self.__processModel = processModel
    # endregion

    # region - Override

    

    # endregion
