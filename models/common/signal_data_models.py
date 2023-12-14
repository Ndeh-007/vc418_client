from typing import Any

from interfaces.structs import ProgramsExplorerActionType, AlertType, TabUpdateType, SystemRequestScope, \
    PreviewToolbarActionType
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


class TreeStructureItemModel:
    def __init__(self, pid: str, parentPid: str, children: list[str], value: str | int, index: int):
        self.__pid: str = pid
        self.__parentPid: str | None = parentPid
        self.__children: list[str] = children
        self.__value = value
        self.__index = index

    def index(self):
        return self.__index

    def value(self):
        return self.__value

    def id(self):
        return self.__pid

    def parentId(self):
        return self.__parentPid

    def children(self):
        return self.__children

    def setID(self, pid: str):
        self.__pid = pid

    def setParentPid(self, pid: str):
        self.__parentPid = pid

    def setChildren(self, pids: list[str]):
        self.__children = pids

    def setValue(self, value: int | str):
        self.__value = value


class TreeStructureModel:
    def __init__(self, rootPID: str | None, structure: dict[str, TreeStructureItemModel]):
        self.__rootPid: str | None = rootPID
        self.__structure: dict[str, TreeStructureItemModel] = structure

    def root(self):
        return self.__rootPid

    def structure(self):
        return self.__structure

    def setRootPid(self, root: str):
        self.__rootPid = root

    def setStructure(self, structure: dict[str, TreeStructureItemModel]):
        self.__structure = structure

    def checkParent(self, childPid: str, parentPid):
        """
        checks if the provided child has the provided parent as its parent.
        returns true if check is true or false otherwise
        :param childPid:
        :param parentPid:
        :return:
        """
        if self.__structure.get(childPid).parentId() == parentPid:
            return True
        else:
            return False
