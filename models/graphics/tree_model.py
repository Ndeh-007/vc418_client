from interfaces.structs import ProgramType, BinaryTreeUpdateMode
from models.common.signal_data_models import TreeStructureModel
from models.explorer.program_item_model import ProgramItemModel
from models.graphics.tree_process_model import TreeProcessModel


class BinaryTreeModel:

    def __init__(self, nProcs: int, structure: TreeStructureModel, program: ProgramType = ProgramType.REDUCE_ERLANG,
                 programItem: ProgramItemModel = None, updateMode: BinaryTreeUpdateMode = BinaryTreeUpdateMode.RUN):
        self.__nProcs: int = nProcs
        self.__treeStructure: TreeStructureModel = structure
        self.__processes: list[TreeProcessModel] = []
        self.__programType: ProgramType = program
        self.__programItem: ProgramItemModel | None = programItem
        self.__updateMode: BinaryTreeUpdateMode = updateMode

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # create the number of processes
        self.constructProcesses()
        # adjust the process nodes levels
        self.adjustNodeLevels()

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

    def adjustNodeLevels(self):
        """
        computes the levels of the nodes such that each node level shows its depth in the binary tree. with all
        processes aligned to the bottom
        this is done by counting backward on the root pid based on the length of the process we want to compute its node
        level
        :return:
        """
        # get the process with most nodes
        root = None
        for p in self.__processes:
            if p.processID() == self.__treeStructure.root():
                root = p
                break
        # use the level values of the root to reassign the levels of other process
        pArr = []
        for p in self.__processes:
            if p.processID() == root.processID():
                pArr.append(p)
                continue
            else:
                for i in range(len(p.nodes())):
                    index = -1 * (i + 1)  # we are indexing the nodes in reverse order
                    node = p.nodes()[index]
                    node.setLevel(root.nodes()[index].level())

    def constructProcesses(self):
        """
        builds processes based on the data provided by the process structure
        no connections are made between these processes.
        :return:
        """
        pidStructure = self.__treeStructure.structure()
        pcs = []

        # build the rest of the processes, without connections
        i = 0
        for pid in pidStructure.keys():
            struct = pidStructure.get(pid)
            model = TreeProcessModel(struct.id(), [], self.__treeStructure, processIndex=i)
            model.createNodes(len(struct.children()) + 1)
            pcs.append(model)
            i += 1
        self.__processes = pcs

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

    def programType(self):
        return self.__programType

    def programItem(self):
        return self.__programItem

    def updateMode(self):
        return self.__updateMode

    # region - Getters

    # endregion

    # region - Setters
    def SetNProcs(self, value: int):
        self.__nProcs = value

    def setProcesses(self, processes: list[TreeProcessModel]):
        self.__processes = processes

    def setProgramItem(self, value: ProgramItemModel | None):
        self.__programItem = value

    def setUpdateMode(self, value: BinaryTreeUpdateMode):
        self.__updateMode = value

    # endregion
