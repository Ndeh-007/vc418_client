from PySide6.QtCore import QSize
from PySide6.QtGui import QImage

from interfaces.structs import ProgramType, ServerType
from models.explorer.program_properties_model import ProgramPropertiesModel


class ProgramItemModel:
    def __init__(self, text: str = None, icon: QImage = None, itemID: str = None,
                 programType: ProgramType = ProgramType.UNDEFINED,
                 properties: ProgramPropertiesModel = None):
        self.__text: str = text

        self.__icon: QImage = icon
        if icon is None:
            self.__icon = QImage(':resources/images/file.ico').scaled(QSize(22, 28))

        self.__programType: ProgramType = programType

        self.__id: str = itemID
        if itemID is None:
            self.__id: str = text.lower().replace(" ", "_")

        self.__props: ProgramPropertiesModel = properties
        if properties is None:
            self.__props: ProgramPropertiesModel = ProgramPropertiesModel()

        self.__serverID = ServerType.ERLANG

    # region getters

    def serverID(self):
        return self.__serverID

    def properties(self):
        return self.__props

    def id(self):
        return self.__id

    def text(self):
        return self.__text

    def icon(self):
        return self.__icon

    def programType(self):
        return self.__programType

    # endregion

    # region setters

    def setProperties(self, props: ProgramPropertiesModel):
        self.__props = props

    def setID(self, itemID: str):
        self.__id = itemID

    def setText(self, text: str):
        self.__text = text

    def setIcon(self, icon: QImage):
        self.__icon = icon

    def setProgramType(self, programType: ProgramType):
        self.__programType = programType

    # endregion
