from typing import Any

from interfaces.structs import ProgramsExplorerActionType, AlertType, TabUpdateType, SystemRequestScope, PreviewToolbarActionType
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


class SystemRequestData:
    def __init__(self, action: Any, content: Any):
        self.action = action
        self.content = content


class SystemRequest:
    def __init__(self, data: SystemRequestData, scope: SystemRequestScope = SystemRequestScope.GLOBAL):
        self.__scope: SystemRequestScope = scope
        self.__data: SystemRequestData = data

    def scope(self):
        return self.__scope

    def data(self):
        return self.__data

    def setScope(self, scope: SystemRequestScope):
        self.__scope = scope

    def setData(self, data: SystemRequestData):
        self.__data = data


class PreviewProgramData:
    def __init__(self, procedure: PreviewToolbarActionType, data: ProgramItemModel):
        self.__data: ProgramItemModel = data
        self.__procedure: PreviewToolbarActionType = procedure

    def data(self):
        return self.__data

    def procedure(self):
        return self.__procedure

    def setData(self, data: ProgramItemModel):
        self.__data = data

    def setProcedure(self, procedure: PreviewToolbarActionType):
        self.__procedure = procedure
