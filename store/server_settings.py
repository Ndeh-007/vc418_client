from interfaces.structs import ServerType
from models.settings.server_model import ServerModel


class ServerSettings:
    """
    Holds server configurations
    """
    def __init__(self):
        self.__servers: dict[str, ServerModel] = {}

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
    def servers(self, target: str = None):
        """
        gets a particular server or all servers as a dict if no target is provided
        :param target:
        :return:
        """
        if target is not None:
            return self.__servers.get(target)

        return self.__servers

    # endregion

    # region - Setters

    def setServers(self, servers: dict[str, ServerModel]):
        """
        sets the server
        :param servers:
        :return:
        """
        self.__servers = servers

    # endregion

    # region - Workers

    def updateServer(self, target: str, server: ServerModel):
        """
        updates the existing servers with a new instance
        :param target:
        :param server:
        :return:
        """
        self.__servers.update({target: server})

    # endregion
