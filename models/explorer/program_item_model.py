import uuid

from PySide6.QtGui import QImage


class ProgramItemModel:
    def __init__(self, text: str = None, icon: QImage = None, itemID: str = None):
        self.__text: str = text
        self.__icon: QImage = icon
        self.__id: str = itemID
        if itemID is None:
            self.__id: str = text.lower().replace(" ", "_")

    # region getters
    def id(self):
        return self.__id

    def text(self):
        return self.__text

    def icon(self):
        return self.__icon

    # endregion

    # region setters
    def setID(self, itemID: str):
        self.__id = itemID

    def setText(self, text: str):
        self.__text = text

    def setIcon(self, icon: QImage):
        self.__icon = icon

    # endregion
