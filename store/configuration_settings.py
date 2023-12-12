from typing import Any


class ConfigurationSettings:
    def __init__(self):
        self.__httpResponseJSONFile = None
        self.__configure()

    # region - Initialize
    def initialize(self, data: dict[str, Any]):
        """
        sets up initial values for all items
        :return:
        """

        self.__httpResponseJSONFile = data.get("httpResponseJSONFile")

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    # endregion

    # region - Workers

    # endregion

    # region - Getters
    def httpResponseJSONFile(self):
        return self.__httpResponseJSONFile
    # endregion

    # region - Setters
    def setHttpResponseJSONFile(self, path: str):
        self.__httpResponseJSONFile = path
    # endregion

    # region - Override

    # endregion

