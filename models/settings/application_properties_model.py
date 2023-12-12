from typing import Any


class ApplicationProperties:
    def __init__(self):
        self.__configuration: dict[str, Any] = {}

    # region - Initialize

    def initialize(self):
        self.__configuration.update({
            "httpResponseJSONFile": "response.json"
        })

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Workers

    # endregion

    # region - Getters
    def configuration(self):
        return self.__configuration

    # endregion

    # region - Setters

    # endregion
