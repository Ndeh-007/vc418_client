from interfaces.structs import ServerType, ServerState


class ServerModel:
    def __init__(self, name: str, serverType: ServerType):
        self.__name: str = name
        self.__type: ServerType = serverType
        self.__state: ServerState = ServerState.OFF
        self.__id: ServerType = serverType

        # self.__command = "C:\\Tools\\rebar3.cmd"
        self.__command = "C:\\Tools\\rebar3.cmd"
        # self.__arguments = ["E:\\Work\\School\\VCS418\\vc418_server", "shell", "--apps", "vc418_server"]
        self.__arguments = ["C:\\Work\\School\\CPSC418\\Project\\vc418_server", "shell", "--apps", "vc418_server"]

    # region - Getters
    def id(self):
        return self.__id

    def state(self):
        return self.__state

    def name(self):
        return self.__name

    def serverType(self):
        return self.__type

    def command(self):
        return self.__command

    def arguments(self):
        return self.__arguments

    # endregion

    # region - Setters
    def setCommand(self, cmd: str):
        self.__command = cmd

    def setArguments(self, args: list[str]):
        self.__arguments = args

    def setstate(self, state: ServerState):
        self.__state = state

    def setName(self, name: str):
        self.__name = name

    def setServerType(self, serverType: ServerType):
        self.__type = serverType

    # endregion
