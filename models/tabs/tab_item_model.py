from PySide6.QtWidgets import QWidget

from models.explorer.program_item_model import ProgramItemModel


class TabItemModel:
    def __init__(self, title: str | None, content: QWidget | None, tabId: str, program: ProgramItemModel):
        self.__title: str = title
        self.__content: QWidget = content
        self.__id: str = tabId
        self.__program: ProgramItemModel = program

    def program(self):
        return self.__program

    def title(self):
        return self.__title

    def content(self):
        return self.__content

    def id(self):
        return self.__id

    def setTitle(self, title: str):
        self.__title = title

    def setProgram(self, program: ProgramItemModel):
        self.__program = program

    def setContent(self, content: QWidget):
        self.__content = content

    def setID(self, tabID: str):
        self.__id = tabID
