from PySide6.QtWidgets import QGraphicsItem


class TreeProcessItemController(QGraphicsItem):
    """
    This graphics item handles a single process.
    each process has its nodes and connectors
    """

    def __init__(self):
        super().__init__()

        self.__parentProcess: TreeProcessItemController | None = None

        self.__childProcesses: list[TreeProcessItemController] = []

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

    # endregion

    # region - Workers

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters

    # endregion

    # region - Setters

    # endregion
