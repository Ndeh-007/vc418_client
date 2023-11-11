from typing import Any

from interfaces.structs import ProgramsExplorerActionType, AlertType, TabUpdateType
from models.explorer.program_item_model import ProgramItemModel


class ProgramExplorerActionModel:
    def __init__(self, data: list[ProgramItemModel] = None, action: ProgramsExplorerActionType = None):
        self.__data: list[ProgramItemModel] = data
        self.__action: ProgramsExplorerActionType = action

    def data(self):
        return self.__data

    def action(self):
        return self.__action

    def setData(self, data: list[ProgramItemModel]):
        self.__data = data

    def setAction(self, action: ProgramsExplorerActionType):
        self.__action = action


class SystemAlert:
    def __init__(self, message: str, alertType: AlertType = AlertType.Error):
        self.__alertType = alertType
        self.__message = message

    def message(self):
        return self.__message

    def alertType(self):
        return self.__alertType

    def setMessage(self, message: str):
        self.__message = message

    def setAlertType(self, alertType: AlertType):
        self.__alertType = alertType


class TabUpdateData:
    def __init__(self, updateType: TabUpdateType, data: Any):
        self.__type = updateType
        self.__data = data

    def updateType(self):
        return self.__type

    def data(self):
        return self.__data

    def setUpdateType(self, updateType: TabUpdateType):
        self.__type = updateType

    def setData(self, data: Any):
        self.__data = data

