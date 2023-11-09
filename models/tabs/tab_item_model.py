from PySide6.QtWidgets import QWidget


class TabItemModel:
    def __init__(self, title: str, content: QWidget, tabId: str):
        self.__title = title
        self.__content = content
        self.__id = tabId

    def title(self):
        return self.__title

    def content(self):
        return self.__content

    def id(self):
        return self.__id

    def setTitle(self, title: str):
        self.__title = title

    def setContent(self, content: QWidget):
        self.__content = content

    def setID(self, tabID: str):
        self.__id = tabID
