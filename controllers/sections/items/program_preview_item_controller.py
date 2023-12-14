from models.explorer.program_item_model import ProgramItemModel
from models.common.signal_data_models import ProgramExplorerActionModel
from views.sections.items.program_preview_item import ProgramPreviewItemView


class ProgramPreviewItemController(ProgramPreviewItemView):
    def __init__(self, model: ProgramExplorerActionModel | ProgramItemModel = None):
        super().__init__()

        self.itemModel = model

        if isinstance(model, ProgramItemModel):
            self.itemModel: ProgramItemModel = model

        if isinstance(model, ProgramExplorerActionModel):
            self.itemModel: ProgramItemModel = model.data()[0]

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        self.controlBar.setItemModel(item=self.itemModel)

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

