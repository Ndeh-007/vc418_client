from typing import Any

from utils.signal_bus import signalBus


class ConfigurationSettings:
    def __init__(self):
        self.__httpResponseJSONFile = None
        self.__animationFrequency = 1
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

    def animationFrequency(self):
        return self.__animationFrequency

    # endregion

    # region - Setters
    def setAnimationFrequency(self, value: int):
        self.__animationFrequency = value
        signalBus.onSettingsFrameRateChanged.emit()

    def setHttpResponseJSONFile(self, path: str):
        self.__httpResponseJSONFile = path
    # endregion

    # region - Override

    # endregion
