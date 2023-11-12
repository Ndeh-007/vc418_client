from interfaces.structs import ServerType, ServerState


class ServerModel:
    def __init__(self, name: str, serverType: ServerType):
        self.__name: str = name
        self.__type: ServerType = serverType
        self.__state: ServerState = ServerState.OFF
        self.__id: ServerType = serverType

    # region - Getters
    def id(self):
        return self.__id

    def state(self):
        return self.__state

    def name(self):
        return self.__name

    def serverType(self):
        return self.__type

    # endregion

    # region - Setters
    def setstate(self, state: ServerState):
        self.__state = state

    def setName(self, name: str):
        self.__name = name

    def setServerType(self, serverType: ServerType):
        self.__type = serverType

    # endregion
