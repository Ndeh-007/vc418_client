import uuid
from typing import Literal

import requests
from PySide6.QtCore import Signal, QObject

from interfaces.structs import ServerType


class HTTPRequestItem(QObject):
    onComplete = Signal(object)
    onError = Signal(object)

    def __init__(self, requestID: str, url: str, programType: str, requestType: Literal['get', 'post'] = 'get',
                 serverID=ServerType.ERLANG):
        super().__init__()

        self.__url: str = url
        self.__requestType: str = requestType
        self.__id = requestID
        self.__pType = programType
        self.__httpResponse: requests.Response | None = None
        self.__serverID = serverID

        self.__initialize()
        self.__configure()

    # region - Initialize
    def __initialize(self):
        pass

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    def __handleFailedRequest(self, response: requests.Response):
        self.onError.emit(f"Failed to fetch data. Status code:{response.status_code}")

    def __handleSuccessfulRequest(self, response: requests.Response):
        data = response.json()
        self.onComplete.emit(data)

    # endregion

    # region - Workers
    def execute(self):
        """
        makes the http request based on the values provided
        :return:
        """
        if self.__requestType == 'get':
            self.__getRequest()

    def __getRequest(self):
        """
        performs a get request
        :return:
        """
        response = requests.get(self.__url)
        self.__httpResponse = response
        if response.status_code == 200:
            self.__handleSuccessfulRequest(response)
        else:
            self.__handleFailedRequest(response)

    # endregion

    # region - Getters
    def serverID(self):
        return self.__serverID

    def httpResponse(self):
        return self.__httpResponse

    def programID(self):
        return self.__pType

    def id(self):
        return self.__id

    def requestType(self):
        return self.__requestType

    def url(self):
        return self.__url

    # endregion

    # region - Setters
    def setRequestType(self, requestType: Literal['get', 'post']):
        self.__requestType = requestType

    def setURL(self, url: str):
        self.__url = url

    # endregion
