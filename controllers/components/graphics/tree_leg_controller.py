from models.graphics.tree_leg_model import TreeLegModel


class TreeLegController:
    def __init__(self, model: TreeLegModel):
        self.__model: TreeLegModel = model

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
    def model(self):
        return self.__model
    # endregion

    # region - Setters
    def setModel(self, model: TreeLegModel):
        self.__model = model
    # endregion

    # region - Override

    # endregion
