from PySide6.QtWidgets import QGraphicsScene

from controllers.components.graphics.tree_process_controller import TreeProcessItemController
from models.common.execution_step_model import ExecutionStepModel
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
        if self.__model is None:
            return
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
        # self.__model.adjustNodeLevels()
        self.__connectProcesses()

    def update(self, scene: QGraphicsScene, executionFrame: ExecutionStepModel):
        """
        we get selected processes and then we update them. the processes to be updated are those whose pids are in the
        current frame
        :param scene:
        :param executionFrame:
        :return:
        """
        # data can either move from parent to child or child to parent
        # and oly the child carries the highway. so we target the child to be updated and we reset the reset
        isParent = self.model().treeStructure().checkParent(executionFrame.source(), executionFrame.target())
        if isParent:
            targetPid = executionFrame.source()
        else:
            targetPid = executionFrame.target()

        for process in self.__processes:
            if process.processModel().processID() == targetPid:
                process.updateDrawing(executionFrame)
            else:
                process.resetDrawing()
        scene.update()

    def draw(self, scene: QGraphicsScene):
        """
        draws the tree on the provided graphics scene. iteratively draws each process.
        at each iteration, it draws the individual process and connects it to its parent.
        :param scene:
        :return:
        """
        for process in self.__processes:
            process.draw(scene)

    # endregion

    # region _local workers

    def __initializeProcesses(self):
        """
        creates processes using data from the provided model.
        if we are updating, we update the controller processes with new data, else we create new process controllers
        :return:
        """
        # if we want to update the values of the processes

        # or we create new controller processes
        pcs = []
        for _pcs in self.__model.processes():
            p = TreeProcessItemController(_pcs)
            pcs.append(p)

        self.__processes = pcs

    def __connectProcessNodes(self):
        for p in self.__processes:
            p.connectNodes()

    def __connectProcesses(self):
        """
        creates relationships between processes and their parents
        :return:
        """
        structure = self.__model.treeStructure()
        struct = structure.structure()

        for key in struct.keys():
            item = struct.get(key)
            # find the proces with the id and set that as the currents parent.
            # we set it to the first available node of the child
            children = item.children()
            for i, child in enumerate(children):
                # define the processes
                childProcess = self.getProcessWithID(child)
                # current = self.getProcessWithID(item.id())

                # get the first node of the child
                childProcessFirstNode = childProcess.nodeAtIndex(0)
                childProcessFirstNodeLevel = childProcessFirstNode.node().level()

                # define the parent process for the child we are working in
                parentProcess = self.getProcessWithID(item.id())
                targetLevel = childProcessFirstNodeLevel - 1
                parentNode = parentProcess.nodeWithAvailableSocket(targetLevel, 1)

                if parentNode is None:
                    continue

                # set the parent of the child node
                childProcessFirstNode.setParentNode(parentNode.node())

                # get the index of the parent node and use it to update is value in the parent process after adjusting
                # its socket value
                parentNode.node().incrementSocket()
                parentProcess.updateNodeWithID(parentNode.node().nodeID(), parentNode)

                # update the entry of the child process
                childProcess.updateNodeAtIndex(0, childProcessFirstNode)

    # endregion

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters
    def model(self):
        return self.__model

    def getProcessWithID(self, target: str):
        item = None
        for p in self.__processes:
            if p.processModel().processID() == target:
                item = p
                break
        return item

    def getProcessIndex(self, process: TreeProcessItemController):
        """
        gets the index of a process.
        :param process:
        :return: index of process, -1 otherwise
        """
        index = -1
        pid = process.processModel().processID()
        for i, p in enumerate(self.__processes):
            if p.processModel().processID() == pid:
                index = i
                break

        return index

    # endregion

    # region - Setters

    def updateProcessWithID(self, pid: str, process: TreeProcessItemController):
        """
        updates process with the provided id
        :param pid:
        :param process:
        :return:
        """
        index = self.getProcessIndex(process)
        if index == -1:
            raise Exception(f"Error updating process in tree_controller. process with id: {pid}, not found")
        self.__processes[index] = process

    def updateProcess(self, process: TreeProcessItemController):
        index = self.getProcessIndex(process)
        if index == -1:
            raise Exception(
                f"Error updating process in tree_controller. process with id: {process.processModel().processID()}, not found")
        self.__processes[index] = process

    def setModel(self, model: BinaryTreeModel):
        self.__model = model
        self.__initializeProcesses()
    # endregion
