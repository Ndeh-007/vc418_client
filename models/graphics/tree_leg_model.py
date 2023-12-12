class TreeLegModel:
    def __init__(self, processID: str, data: str = None, legWidth: int = 10, legHeight: int = 10):
        self.__processID: str = processID
        self.__data: str = data
        self.__width: int = legWidth
        self.__height: int = legHeight

    # region - Workers

    # endregion

    # region - Getters
    def processID(self):
        return self.__processID

    def data(self):
        return self.__data

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    # endregion

    # region - Setters
    def setData(self, value: str):
        self.__data = value

    def setWidth(self, value: int):
        self.__width = value

    def setHeight(self, value: int):
        self.__height = value

    def setProcessID(self, value: str):
        self.__processID = value

    # endregion
