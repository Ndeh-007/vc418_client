from ctypes import Union
from typing import Any

import PySide6
from PySide6.QtCore import QAbstractListModel
from PySide6 import QtCore, QtGui, QtWidgets

from models.explorer.program_item_model import ProgramItemModel


class ProgramListModel(QAbstractListModel):
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
