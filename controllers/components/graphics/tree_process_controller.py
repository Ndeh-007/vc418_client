from PySide6.QtCore import QRect, QPoint, QSize, QRectF, QSizeF, QPointF, QLine
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsLineItem

from controllers.components.graphics.tree_highway_controller import TreeHighwayController
from controllers.components.graphics.tree_node_controller import TreeNodeItemController
from models.common.execution_step_model import ExecutionStepModel
from models.graphics.tree_highway_model import TreeHighwayModel
from models.graphics.tree_process_model import TreeProcessModel
from utils.helpers import getPidNumber


class TreeProcessItemController(QGraphicsItem):
    """
    This graphics item handles a single process.
    each process has its nodes and connectors
    """

    def __init__(self, processModel: TreeProcessModel = None):
        super().__init__()

        self.__processModel: TreeProcessModel = processModel
        self.__nodes: list[TreeNodeItemController] = []
        self.__highways: list[TreeHighwayController] = []  # we keep only the connections between two processes

        self.__baseRect = QRect(QPoint(0, 0), QSize(10, 10))
        self.__padding = QSize(5, 5)

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        """
        set up values of the controller
        1. create the various nodes
        :return:
        """
        self.__createNodes()

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    # endregion

    # region - Workers

    def updateDrawing(self, scene: QGraphicsScene, executionFrame: ExecutionStepModel):
        """
        updates the process drawing on the canvas
        :param scene:
        :param executionFrame:
        :return:
        """
        for highway in self.__highways:
            case1 = highway.model().fromPid() == executionFrame.source() and highway.model().toPid() == executionFrame.target()
            case2 = highway.model().fromPid() == executionFrame.target() and highway.model().toPid() == executionFrame.source()

            # indicate that we want to update
            highway.prepareGeometryChange()

            # perform the required update modifications
            if case1 or case2:
                # update
                # we leverage the fact that the pids are in the order <0.1.0>, <0.2.0>, <0.3.0> ..., <0.n.0>
                # check if we are moving left or right
                source = getPidNumber(executionFrame.source())
                target = getPidNumber(executionFrame.target())

                if source is None or target is None:
                    continue

                if source > target:
                    # we are moving left
                    direction = "left"
                else:
                    # we are moving right
                    direction = "right"

                # update the desired properties
                highway.model().setArrowDirection(direction)
                highway.model().setData(executionFrame.data())
            else:
                # reset highway data
                highway.reset()

            # trigger the redraw
            highway.update()

    def draw(self, scene: QGraphicsScene):
        """
        draws the current process on the scene. it adds the nodes to the scene and then draws line connecting the nodes
        :param scene:
        :return:
        """
        for graphicsNodeItem in self.__nodes:
            # add the node to the scene
            scene.addItem(graphicsNodeItem)

            # add a line between the current node and its parent node
            # if the parent does not exist, we move to the next node
            parentNode = graphicsNodeItem.parentNode()
            if parentNode is None:
                continue
            else:
                # we check if the parent node and the child node have the same process
                # if they have the same process, we draw an empty line, else we draw a line with arrow allocations

                # we also have to check the direction from which the data is coming in order to draw the correct arrow.
                # for now we will leave it like that just ot see how the highway works
                if parentNode.processID() == graphicsNodeItem.node().processID():
                    highwayModel = TreeHighwayModel(
                        fromAnchor=graphicsNodeItem.node().top(),
                        toAnchor=parentNode.bottom(),
                        fromPid=graphicsNodeItem.node().processID(),
                        toPid=parentNode.processID(),
                        thickness=1
                    )
                    highwayController = TreeHighwayController(highwayModel)
                    scene.addItem(highwayController)

                else:

                    highwayModel = TreeHighwayModel(
                        fromAnchor=graphicsNodeItem.node().top(),
                        toAnchor=parentNode.bottom(),
                        fromPid=graphicsNodeItem.node().processID(),
                        toPid=parentNode.processID(),
                        data=None,
                        leftArrow=QPixmap(":resources/images/arrow-left.png"),
                        rightArrow=QPixmap(":resources/images/arrow-right.png"),
                        thickness=1,
                    )
                    highwayController = TreeHighwayController(highwayModel)
                    highwayController.setTrafficDirection(None)
                    scene.addItem(highwayController)
                    self.__highways.append(highwayController)

    def __createNodes(self):
        """
        creates controller nodes based on the models provided
        :return:
        """
        cNodes = []
        nodes = self.__processModel.nodes()

        # create the rest of the nodes otherwise
        for i in range(0, len(nodes)):
            vShift = int(nodes[i].vOffsetFactor() * nodes[i].level())
            hShift = int(self.__processModel.processIndex() * nodes[i].hOffsetFactor())
            n = TreeNodeItemController(processID=self.__processModel.processID(),
                                       parentNode=None,
                                       rect=QRect(
                                           QPoint(hShift + self.__baseRect.left(), vShift + self.__baseRect.bottom()),
                                           self.__baseRect.size()
                                       ),
                                       parent=self, model=nodes[i])
            # n.setNode(nodes[i])
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

    def nodes(self):
        return self.__nodes

    def nodeIndex(self, node: TreeNodeItemController):
        """
        gets the index of node
        :param node:
        :return:
        """
        index = -1
        for i, n in enumerate(self.__nodes):
            if n.node().nodeID() == node.node().nodeID():
                index = i
        return index

    def nodeAtIndex(self, index: int):
        return self.__nodes[index]

    def nodeAtLevel(self, level: int):
        node = None
        for n in self.__nodes:
            if n.node().level() == level:
                node = n
        return node

    def nodeWithAvailableSocket(self, targetLevel: int, targetSocket: int = 1):
        """
        A recursive function call that climbs up a process node by node until it finds a socket with value equal that
        provided by the target socket.
        :param targetLevel: the level from which we start checking from.
        :param targetSocket: the node whose socket value is this
        :return:
        """

        node = self.nodeAtLevel(targetLevel)
        if node.node().socket() == targetSocket:
            return node
        else:
            return self.nodeWithAvailableSocket(targetLevel - 1, targetSocket)

    # endregion

    # region - Setters
    def setProcessModel(self, processModel: TreeProcessModel):
        self.__processModel = processModel

    def setNodes(self, nodes: list[TreeNodeItemController]):
        self.__nodes = nodes

    def updateNodeAtIndex(self, index: int, node: TreeNodeItemController):
        self.__nodes[index] = node

    def updateNodeWithID(self, nodeId: str, node: TreeNodeItemController):
        """
        updates node with the provided index
        :param nodeId:
        :param node:
        :return:
        """
        idx = None
        for i, n in enumerate(self.__nodes):
            if n.node().nodeID() == nodeId:
                idx = i
                break
        self.__nodes[idx] = node

    # endregion

    # region - Override

    # region - Override Helpers

    def __computeBoundingRect(self) -> QRectF:
        """
        sum the node heights and the distance between nodes plus the foot height. for the width, the maximum vvalue of the node and foot.
        the anchor point of the bounding rect should have take top left position of the 1st node of that process and then adds a padding
        :return:
        """
        h = sum([item.rect().size().height() for item in self.__nodes] + [
            (self.__nodes[0].node().hOffsetFactor() * (len(self.__nodes) - 1))])
        w = max([item.rect().size().width() for item in self.__nodes])

        return QRectF(
            QPointF(
                float(self.__nodes[0].rect().left() - self.__padding.width()),
                float(self.__nodes[0].rect().top() - self.__padding.height()),
            ),
            QSizeF(float(w), float(h))
        )

    # endregion

    def boundingRect(self) -> QRectF:
        return self.__computeBoundingRect()

    # def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = ...) -> None:

    # endregion
