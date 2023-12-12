from typing import Any

from PySide6.QtCore import QLine
from PySide6.QtWidgets import QGraphicsLineItem

from controllers.components.graphics.tree_controller import TreeGraphicsItemController
from models.common.execution_step_model import ExecutionStepModel
from models.graphics.tree_model import BinaryTreeModel
from utils.signal_bus import signalBus
from views.components.tab_preview_canvas_view import TabPreviewCanvasView


class TabPreviewCanvasController(TabPreviewCanvasView):
    def __init__(self):
        super().__init__()

        self.binaryTree = TreeGraphicsItemController()

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # set the scene of the graphics view
        self.graphicsView.setScene(self.scene)

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
        self.binaryTree.setModel(model)

        # construct the tree
        self.binaryTree.constructTree()

        # draw the tree
        self.binaryTree.draw(self.scene)
        print("drawing complete", len(self.scene.items()))

    def __handleTreeUpdate(self, playbackFrame: ExecutionStepModel):
        self.binaryTree.update(self.scene, playbackFrame)
        signalBus.onLogToOutput.emit(f"frame received: {playbackFrame.data()} [FROM] {playbackFrame.source()}, [TO] {playbackFrame.target()}")
    # endregion

    # region - Workers

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

    # endregion

