from PySide6.QtGui import QImage


class ProgramItemModel:
    def __init__(self, text: str = None, icon: QImage = None):
        self.__text = text
        self.__icon = icon

    # region getters
    def text(self):
        return self.__text

    def icon(self):
        return self.__icon

    # endregion

    # region setters

    def setText(self, text: str):
        self.__text = text

    def setIcon(self, icon: QImage):
        self.__icon = icon

    # endregion
