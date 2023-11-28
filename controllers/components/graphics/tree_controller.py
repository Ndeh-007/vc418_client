from controllers.components.graphics.tree_process_controller import TreeProcessItemController
from models.graphics.tree_model import BinaryTreeModel


class TreeGraphicsItemController:
    """
    handles the tree processes,
    This graphicsItem holds the tree which will be drawn on the main canvas.

    """

    def __init__(self, model: BinaryTreeModel = None):
        self.__model = model
        self.__processes: list[TreeProcessItemController] = []

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        self.__initializeProcesses()

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    # endregion

    # region - Workers

    # region public workers

    def constructTree(self):
        self.__connectProcessNodes()
        self.__connectProcesses()

    # endregion

    # region _local workers

    def __initializeProcesses(self):
        """
        creates processes using data from the provided model
        :return:
        """
        pcs = []

        for _pcs in self.__model.processes():
            p = TreeProcessItemController(_pcs)
            pcs.append(p)

        self.__processes = pcs

    def __connectProcessNodes(self):
        pass

    def __connectProcesses(self):
        pass

    # endregion

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion
    def model(self):
        return self.__model

    # region - Getters

    # endregion

    # region - Setters

    def setModel(self, model: BinaryTreeModel):
        self.__model = model

    # endregion
