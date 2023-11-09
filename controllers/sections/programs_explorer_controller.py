from PySide6.QtGui import QImage

from interfaces.structs import ProgramsExplorerActionType, AlertType
from models.explorer.program_item_model import ProgramItemModel
from models.explorer.programs_list_model import ProgramListModel
from models.signal_data_models import ProgramExplorerActionModel, SystemAlert
from utils.signal_bus import signalBus
from views.sections.programs_explorer import ProgramsExplorerView


class ProgramsExplorerController(ProgramsExplorerView):
    def __init__(self):
        super().__init__()
        self.model = ProgramListModel()
        self.programsListView.setModel(self.model)

        self.initialize()
        self.configure()

    # region - Initialize

    def initialize(self):
        file = QImage(':resources/images/file.png')
        data = [
            ProgramItemModel("File 1", file),
            ProgramItemModel("File 2", file),
            ProgramItemModel("File 3", file),
            ProgramItemModel("File 4", file),
            ProgramItemModel("File 4", file),
        ]
        self.model.addItems(data)

    # endregion

    # region - configure

    def configure(self):
        """
        connect required slots and signals
        :return:
        """
        self.programsListView.onItemClicked.connect(self.__handleListItemClicked)
        self.programsListView.onContextMenuAction.connect(self.__handleContextMenuActions)

    # end region

    # region - Event Handlers

    def __handleListItemDoubleClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        if options.action() == ProgramsExplorerActionType.Open:
            pass


    def __handleListItemClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        try:
            if options.action() == ProgramsExplorerActionType.Select:
                item = options.data()[0]
                signalBus.onSystemAlert.emit(SystemAlert(item.text(), AlertType.Event))
            else:
                signalBus.onSystemAlert.emit(SystemAlert("Invalid Selection Option, see console"))
                signalBus.onLogToOutput.emit(f"Expected `Select` option, got {options.action()} instead.")
        except Exception as e:
            signalBus.onSystemAlert.emit(SystemAlert("Invalid Selection Option, see console"))
            signalBus.onLogToOutput.emit(f"[Error] {str(e)}")

    def __handleContextMenuActions(self, options: ProgramExplorerActionModel):
        pass

    # endregion
