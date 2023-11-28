from PySide6.QtCore import QObject, Signal

from interfaces.structs import AlertType, ServerState, ServerType
from models.settings.http_request_item import HTTPRequestItem
from models.settings.process_manager import ProcessItem
from models.common.signal_data_models import SystemAlert
from utils.helpers import changeServerState
from utils.signal_bus import signalBus

import store.settings as ss


class HTTPRequestManager(QObject):
    onError = Signal(str)

    def __init__(self):
        super().__init__()

        self.__requests: dict[str, HTTPRequestItem] = {}
        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        pass

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    def __handleNewHTTPRequest(self, request: HTTPRequestItem):
        """
        updates the list o requests and then launches the request
        :param request:
        :return:
        """
        self.updateRequest(request.id(), request)
        self.launchRequest(request.id())

    # endregion

    # region - Workers
    def removeRequest(self, target: str):
        """
        removes and returns request with the provided id
        :param target:
        :return:
        """
        return self.__requests.pop(target)

    def launchRequest(self, target: str):
        """
        launches a request with the provided key. first check if the server is alive.
        if the server is alive, execute target, else raise warning.
        :param target:
        :return:
        """
        r = self.__requests.get(target)

        if not self.__checkServer(r.serverID()):
            msg = "Fetch failed. Launch corresponding server and try again."
            alert = SystemAlert(msg, AlertType.Warning)
            signalBus.onSystemAlert.emit(alert)
            self.onError.emit(msg)
            return

        # instantiate the fetch as subprocess
        p = ProcessItem(r.id(), self.__launchRequestWorker, r, onCompleteTask=self.__lRW_Complete, onStartTask=self.__lRW_Start)
        signalBus.onSystemProcess.emit(p)

    @staticmethod
    def __launchRequestWorker(r: HTTPRequestItem):
        # execute the request
        r.execute()

    @staticmethod
    def __lRW_Complete(_):
        # revert the server state
        changeServerState(ServerType.ERLANG, ServerState.ON)

    @staticmethod
    def __lRW_Start():
        # revert the server state
        changeServerState(ServerType.ERLANG, ServerState.WORKING)

    @staticmethod
    def __checkServer(serverID: str):
        """
        checks if the server for the provided program id is ON or off
        :param serverID:
        :return:
        """
        server = ss.APP_SETTINGS.SERVER.servers(target=serverID)
        if server is None:
            return False

        if server.state() == ServerState.ON:
            return True
        else:
            return False

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        signalBus.onHTTPRequest.connect(self.__handleNewHTTPRequest)

    # endregion

    # region - Getters
    def request(self, target: str = None):
        """
        gets a particular request or get all requests
        :param target:
        :return:
        """
        if target is not None:
            return self.__requests.get(target)
        return self.__requests

    def requestByProgramID(self, target: str = None):
        """
        gets items based on their program_id. if item is not found, return None
        :param target:
        :return:
        """
        res = []
        for key in self.__requests.keys():
            item = self.__requests.get(key)
            if target == item.programID():
                res.append(item)
        return res

    # endregion

    # region - Setters
    def updateRequest(self, target: str, item: HTTPRequestItem):
        """
        updates or create a new request
        :param target:
        :param item:
        :return:
        """
        self.__requests.update({target: item})

    def setRequests(self, requests: dict[str, HTTPRequestItem]):
        """
        sets all the values of the requests
        :param requests:
        :return:
        """
        self.__requests = requests

    # endregion
