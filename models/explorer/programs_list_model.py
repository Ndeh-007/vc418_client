from ctypes import Union
from typing import Any

import PySide6
from PySide6.QtCore import QAbstractListModel, QObject, Signal
from PySide6 import QtCore, QtGui, QtWidgets
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

    def addItems(self, items: list[ProgramItemModel]):
        for i, item in enumerate(items):
            self.items.append(item)

    def flags(self, index: PySide6.QtCore.QModelIndex) -> PySide6.QtCore.Qt.ItemFlag:
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    def getDataAtIndex(self, index: PySide6.QtCore.QModelIndex):
        return self.items[index.row()]
