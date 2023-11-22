from interfaces.structs import ServerType
from models.settings.server_model import ServerModel
from models.settings.server_process_model import ServerProcessModel
from utils.signal_bus import signalBus


class ServerSettings:
    """
    Holds server configurations;
    """

    def __init__(self):
        self.__servers: dict[ServerType, ServerModel] = {}
        self.__serverProcesses: dict[ServerType, ServerProcessModel] = {}

    # region - Initialize

    def initialize(self):
        """
        sets up the initial state of the server
        :return:
        """

        erlangServer = ServerModel("Erlang", ServerType.ERLANG)

        self.__servers = {
            erlangServer.id(): erlangServer,
        }

    # endregion

    # region - Getters

    def servers(self, target: ServerType = None):
        """
        gets a particular server or all servers as a dict if no target is provided
        :param target:
        :return:
        """
        if target is not None:
            return self.__servers.get(target)

        return self.__servers

    def serverProcesses(self, target: ServerType):
        if target is not None:
            return self.__serverProcesses.get(target)

        return self.__serverProcesses

    # endregion

    # region - Setters

    def setServerProcesses(self, processes: dict[ServerType, ServerProcessModel]):
        self.__serverProcesses = processes

    def setServers(self, servers: dict[ServerType, ServerModel]):
        """
        sets the server
        :param servers:
        :return:
        """
        self.__servers = servers

    # endregion

    # region - Workers
    def updateServerProcess(self, target: ServerType, process: ServerProcessModel):
        """
        updates the existing servers with a new instance
        :param target:
        :param process:
        :return:
        """
        self.__serverProcesses.update({target: process})

    def updateServer(self, target: ServerType, server: ServerModel):
        """
        updates the existing servers with a new instance
        :param target:
        :param server:
        :return:
        """
        self.__servers.update({target: server})
        self.signalUpdate(server)

    # endregion

    # region signalling
    @staticmethod
    def signalUpdate(server: ServerModel):
        signalBus.onServerStatusChanged.emit(server)

    # endregion
