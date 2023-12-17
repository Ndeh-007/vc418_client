from typing import Literal

from PySide6.QtGui import QWheelEvent, QTransform

from controllers.components.graphics.tree_controller import TreeGraphicsItemController
from models.common.execution_step_model import ExecutionStepModel
from models.graphics.tree_model import BinaryTreeModel
from utils.signal_bus import signalBus
from views.components.tab_preview_canvas_view import TabPreviewCanvasView


class TabPreviewCanvasController(TabPreviewCanvasView):
    def __init__(self):
        super().__init__()
        self.__maxScroll = 500
        self.__minScroll = 0
        self.__currentScale = 250

        self.binaryTree = TreeGraphicsItemController()

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # set the scene of the graphics view
        # activeProgramFile = ss.APP_SETTINGS.PROGRAMS.activeProgram()
        pass

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers
    def __handleTreeModel(self, model: BinaryTreeModel):
        """
        uses the binary tree model to construct a tree and then draws the tree
        :param model:
        :return:
        """
        if self.binaryTree.model() is None:
            self.binaryTree.setModel(model)

        #  if the incoming model is not a reload, and we are running on the same file
        check1 = model.programItem().id() == self.binaryTree.model().programItem().id()

        print(f"check1 => {check1} \n")

        if check1:
            # update the scene with his data
            # clear the scene before the drawing the new tree
            self.scene.clear()

            # set up the binary tree model
            self.binaryTree.setModel(model)

            # construct the tree
            self.binaryTree.constructTree()

            # draw the tree
            self.binaryTree.draw(self.scene)
            print("drawing complete", len(self.scene.items()))

    def __handleTreeUpdate(self, playbackFrame: ExecutionStepModel):
        self.binaryTree.update(self.scene, playbackFrame)
        signalBus.onLogToOutput.emit(
            f"frame received: {playbackFrame.data()} [FROM] {playbackFrame.source()}, [TO] {playbackFrame.target()}")

    # endregion

    # region - Workers

    # region - Public Workers
    def updateCanvasScale(self, mode: Literal['zoom-in', 'zoom-out', 'reset']):
        """
        slot for handling the canvas scaling
        :param mode:
        :return:
        """
        if mode == "zoom-in":
            dy = 12
            if self.__testZoomState(dy):
                self.__setupScaleMatrix(dy)
        if mode == "zoom-out":
            dy = -12
            if self.__testZoomState(dy):
                self.__setupScaleMatrix(dy)
        if mode == "reset":
            dy = 50
            self.__setupScaleMatrix(dy, True)

    # endregion

    # region - Private workers

    def __testZoomState(self, value) -> bool:
        """
        tests if the scaling is in the required range
        :return:
        """
        if self.__minScroll <= self.__currentScale + value <= self.__maxScroll:
            return True
        else:
            return False

    def __setupScaleMatrix(self, value, isReset=False):
        self.__currentScale += value
        if isReset:
            self.__currentScale = value
        scale = pow(2, (self.__currentScale - 250) / 50)
        matrix = QTransform()
        matrix.scale(scale, scale)
        self.setTransform(matrix)

    # endregion

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        signalBus.onLoadTreeModel.connect(self.__handleTreeModel)
        signalBus.onUpdateTree.connect(self.__handleTreeUpdate)

    # endregion

    # region - Getters

    # endregion

    # region - Setters

    # endregion

    # region - Override
    def wheelEvent(self, event: QWheelEvent) -> None:
        super().wheelEvent(event)

        dy = event.angleDelta().y() / 10
        if self.__testZoomState(dy):
            self.__setupScaleMatrix(dy)
    # endregion
