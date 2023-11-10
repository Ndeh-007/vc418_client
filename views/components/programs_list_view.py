from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QMouseEvent, Qt, QContextMenuEvent, QAction
from PySide6.QtWidgets import QListView, QMenu

from interfaces.structs import ProgramsExplorerActionType
from models.explorer.program_item_model import ProgramItemModel
from models.signal_data_models import ProgramExplorerActionModel


class ProgramsListContextMenu(QMenu):
    def __init__(self):
        super().__init__()

        # define the actions
        newAction = QAction("New Program", self)
        deleteAction = QAction("Delete", self)
        runAction = QAction("Run", self)

        # attach action data
        newAction.setData(ProgramsExplorerActionType.New)
        deleteAction.setData(ProgramsExplorerActionType.Delete)
        runAction.setData(ProgramsExplorerActionType.Run)

        # add actions to menu
        self.addAction(newAction)
        self.addSeparator()
        self.addAction(runAction)
        self.addSeparator()
        self.addAction(deleteAction)


class ProgramsListView(QListView, QObject):
    onContextMenuAction = Signal(ProgramExplorerActionModel)
    onItemClicked = Signal(ProgramExplorerActionModel)
    onItemDoubleClicked = Signal(ProgramExplorerActionModel)

    def __init__(self):
        super().__init__()

        self.contextMenu = ProgramsListContextMenu()

        self.configure()

    # region - configure
    def configure(self):
        self.contextMenu.triggered.connect(self.__handleMenuTriggered)

    # endregion

    # region - override

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        super().mouseDoubleClickEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            item = self.model().getDataAtIndex(self.selectedIndexes()[0])
            data = ProgramExplorerActionModel([item], ProgramsExplorerActionType.Open)
            self.onItemDoubleClicked.emit(data)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            item = self.model().getDataAtIndex(self.selectedIndexes()[0])
            data = ProgramExplorerActionModel([item], ProgramsExplorerActionType.Select)
            self.onItemClicked.emit(data)

    def contextMenuEvent(self, arg__1: QContextMenuEvent) -> None:
        self.contextMenu.exec(arg__1.globalPos())

    # endregion

    # region - event handlers

    def __handleMenuTriggered(self, action: QAction):
        """
        get the selected item and the action to be performed on that item and send.
        :param action:
        :return:
        """
        actionType = action.data()
        items = []
        for index in self.selectedIndexes():
            items.append(self.model().itemData(index))

        data = ProgramExplorerActionModel(items, actionType)
        self.onContextMenuAction.emit(data)

    # endregion
