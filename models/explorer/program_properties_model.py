class ProgramPropertiesModel:
    def __init__(self, nProcs: int = 4):
        self.__nProcs: int = nProcs

    # region - Initialize

    def initialize(self, data):
        # sets the setting values for base program properties
        pass

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    # endregion

    # region - Workers

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters
    def nProcs(self):
        return self.__nProcs

    # endregion

    # region - Setters
    def setNProcs(self, value: int):
        self.__nProcs: int = value

    # endregion
