from models.common.signal_data_models import TreeStructureModel
from models.graphics.tree_node_model import TreeNodeModel


class TreeProcessModel:
    def __init__(self, pid: str, nodes: list[TreeNodeModel], treeStructure: TreeStructureModel, processIndex: int = 0):
        self.__processID: str = pid
        self.__processIndex: int = processIndex
        self.__nodes: list[TreeNodeModel] = nodes
        self.__tree: TreeStructureModel = treeStructure

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
    def createNodes(self, qty: int):
        """
        creates nodes for this process. from top to bottom.
        :param qty:
        :return:
        """
        nodes = []

        for i in range(qty):
            n = TreeNodeModel(self.__processID, 1, i)
            nodes.append(n)

        self.__nodes = nodes

    # endregion

    # region - Workers

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters
    def processIndex(self):
        return self.__processIndex

    def tree(self):
        return self.__tree

    def processID(self):
        return self.__processID

    def nodes(self):
        return self.__nodes

    def nodeAtIndex(self, index: int):
        return self.__nodes[index]

    def nodeWithID(self, nodeID: str):
        _node = None
        for node in self.__nodes:
            if node.nodeID() == nodeID:
                _node = node
                break
        return _node

    # endregion

    # region - Setters

    def setProcessIndex(self, index: int):
        self.__processIndex = index

    def setNodes(self, node: list[TreeNodeModel]):
        self.__nodes = node

    def addNode(self, node: TreeNodeModel):
        self.__nodes.append(node)

    def updateNodeAtIndex(self, index: int, node: TreeNodeModel):
        self.__nodes[index] = node

    def updateNodeWithID(self, node: TreeNodeModel, nodeID: str):
        index = 0
        for i, node in enumerate(self.__nodes):
            if node.nodeID() == nodeID:
                index = i
                break

        self.updateNodeAtIndex(index, node)

    # endregion
