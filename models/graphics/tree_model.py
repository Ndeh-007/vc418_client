from models.common.signal_data_models import TreeStructureModel
from models.graphics.tree_process_model import TreeProcessModel


class BinaryTreeModel:

    def __init__(self, nProcs: int, structure: TreeStructureModel):
        self.__nProcs: int = nProcs
        self.__treeStructure: TreeStructureModel = structure
        self.__processes: list[TreeProcessModel] = []

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # create the number of processes
        self.constructProcesses()

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    # endregion

    # region - Workers
    def connectProcesses(self):
        """
        establishes connections based on the tree structure provided
        :return:
        """
        pass

    def constructProcesses(self):
        """
        builds processes based on the data provided by the process structure
        no connections are made between these processes.
        :return:
        """
        pidStructure = self.__treeStructure.structure()

        # build the rest of the processes, without connections
        for pid in pidStructure.keys():
            struct = pidStructure.get(pid)
            model = TreeProcessModel(struct.id(), [], self.__treeStructure)
            model.createNodes(len(struct.children()) + 1)
            self.__processes.append(model)

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion
    def nProcs(self):
        return self.__nProcs

    def treeStructure(self):
        return self.__treeStructure

    def processes(self):
        return self.__processes

    # region - Getters

    # endregion

    # region - Setters
    def SetNProcs(self, value: int):
        self.__nProcs = value

    def setProcesses(self, processes: list[TreeProcessModel]):
        self.__processes = processes

    # endregion
