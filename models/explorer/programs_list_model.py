from typing import Any

import PySide6
from PySide6 import QtGui
from PySide6.QtCore import QAbstractListModel, QObject, QModelIndex, Signal, Slot
from PySide6.QtGui import Qt

from models.explorer.program_item_model import ProgramItemModel


class ProgramListModel(QAbstractListModel, QObject):

    def __init__(self, items: list[ProgramItemModel] = None):
        super().__init__()

        self.items: list[ProgramItemModel] = items
        if items is None:
            self.items: list[ProgramItemModel] = []

    def data(self, index: PySide6.QtCore.QModelIndex, role: int = ...) -> Any:
        item = self.items[index.row()]
        if role == QtGui.Qt.ItemDataRole.DisplayRole:
            return item.text()

        if role == QtGui.Qt.ItemDataRole.DecorationRole:
            return item.icon()

    def rowCount(self, parent: PySide6.QtCore.QModelIndex = ...) -> int:
        return len(self.items)

    def flags(self, index: PySide6.QtCore.QModelIndex) -> PySide6.QtCore.Qt.ItemFlag:
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    def getDataAtIndex(self, index: PySide6.QtCore.QModelIndex):
        if index.row() >= len(self.items):
            return None
        return self.items[index.row()]

    def updateItem(self, data: ProgramItemModel):
        """
        matches by id and updates
        :param data:
        :return:
        """
        for item in self.items:
            if item.id() == data.id():
                item.setText(data.text())
                break
