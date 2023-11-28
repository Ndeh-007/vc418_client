from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QMouseEvent, Qt, QContextMenuEvent, QAction
from PySide6.QtWidgets import QListView, QMenu

from interfaces.structs import ProgramsExplorerActionType
from models.common.signal_data_models import ProgramExplorerActionModel
from utils.styling import q_read_style


class ProgramsListContextMenu(QMenu):
    def __init__(self):
        super().__init__()

        # define the actions
        newAction = QAction("New ...", self)
        deleteAction = QAction("Delete", self)
        runAction = QAction("Run", self)
        renameAction = QAction("Rename", self)

        # attach action data
        newAction.setData(ProgramsExplorerActionType.New)
        deleteAction.setData(ProgramsExplorerActionType.Delete)
        runAction.setData(ProgramsExplorerActionType.Run)
        renameAction.setData(ProgramsExplorerActionType.Rename)

        # add actions to menu
        self.addAction(newAction)
        self.addSeparator()
        self.addAction(renameAction)
        self.addSeparator()
        self.addAction(deleteAction)

        self.setStyleSheet(q_read_style("context-menu"))


class ProgramsListView(QListView, QObject):
    onContextMenuAction = Signal(ProgramExplorerActionModel)
    onItemClicked = Signal(ProgramExplorerActionModel)
    onItemDoubleClicked = Signal(ProgramExplorerActionModel)
    onError = Signal(str)

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
            indexes = self.selectedIndexes()
            if len(indexes) == 0:
                return
            item = self.model().getDataAtIndex(indexes[0])
            if item is None:
                return
            data = ProgramExplorerActionModel([item], ProgramsExplorerActionType.Open)
            self.onItemDoubleClicked.emit(data)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            if len(self.selectedIndexes()) == 0:
                return

            if self.model().rowCount() == 0:
                return

            item = self.model().getDataAtIndex(self.selectedIndexes()[0])
            if item is None:
                return
            data = ProgramExplorerActionModel([item], ProgramsExplorerActionType.Select)
            self.onItemClicked.emit(data)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        self.contextMenu.exec(event.globalPos())

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
            item = self.model().getDataAtIndex(index)
            if item is None:
                continue
            items.append(item)

        data = ProgramExplorerActionModel(items, actionType)
        self.onContextMenuAction.emit(data)

    # endregion
