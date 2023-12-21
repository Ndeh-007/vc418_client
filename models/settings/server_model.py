from typing import Literal
import re

from interfaces.structs import ServerType, ServerState


class ServerModel:
    def __init__(self, name: str, serverType: ServerType):
        self.__name: str = name
        self.__type: ServerType = serverType
        self.__state: ServerState = ServerState.OFF
        self.__id: ServerType = serverType
        self.__port: int = 8080
        self.__domain: str = "localhost"
        self.__httpMode: Literal["http", "https"] = "http"
        self.__url = f"{self.__httpMode}://{self.__domain}:{self.__port}/"

        # self.__command = "C:\\Tools\\rebar3\\rebar3.cmd"
        # self.__command = "C:\\Tools\\rebar3.cmd"
        self.__command = "rebar3.cmd"
        self.__arguments = ["E:\\Work\\School\\VCS418\\vc418_server", "shell", "--apps", "vc418_server"]
        # self.__arguments = ["C:\\Work\\School\\CPSC418\\Project\\vc418_server", "shell", "--apps", "vc418_server"]

    # region - Getters

    def url(self):
        return f"{self.__httpMode}://{self.__domain}:{self.__port}/"

    def port(self):
        return self.__port

    def domain(self):
        return self.__domain

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
    def setUrl(self, url: str):
        if self.__checkURL(url):
            self.__url = url
        else:
            raise Exception("Provided invalid URL")

    def setPort(self, port: int):
        self.__port = port

    def setHTTPMode(self, mode: Literal["http", "https"]):
        self.__httpMode = mode

    def setDomain(self, domain: str):
        self.__domain = domain

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

    # region workers
    @staticmethod
    def __checkURL(url: str):
        # Define the regex pattern for the given format
        pattern = r"^(https?://)(localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(:\d{1,5})?$"

        # Check if the input string matches the pattern
        if re.match(pattern, url):
            return True
        else:
            return False

    # endregion
