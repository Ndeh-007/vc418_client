import uuid

from PySide6.QtGui import QImage

from controllers.sections.items.program_preview_item_controller import ProgramPreviewItemController
from interfaces.structs import ProgramsExplorerActionType, AlertType
from models.explorer.program_item_model import ProgramItemModel
from models.explorer.programs_list_model import ProgramListModel
from models.signal_data_models import ProgramExplorerActionModel, SystemAlert
from models.tabs.tab_item_model import TabItemModel
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
            ProgramItemModel("File 1", file, str(uuid.uuid4())),
            ProgramItemModel("File 2", file, str(uuid.uuid4())),
            ProgramItemModel("File 3", file, str(uuid.uuid4())),
            ProgramItemModel("File 4", file, str(uuid.uuid4())),
            ProgramItemModel("File 4", file, str(uuid.uuid4())),
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
        self.programsListView.onItemDoubleClicked.connect(self.__handleListItemDoubleClicked)
        self.programsListView.onContextMenuAction.connect(self.__handleContextMenuActions)

    # end region

    # region - Event Handlers

    def __handleListItemDoubleClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        if options.action() == ProgramsExplorerActionType.Open:
            # construct the widget
            w = ProgramPreviewItemController()
            t = options.data()[0].text()
            tabModel = TabItemModel(t, w, options.data()[0].id())
            self.__openTab(tabModel)

    def __handleListItemClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        # try:
        #     if options.action() == ProgramsExplorerActionType.Select:
        #         item = options.data()[0]
        #         signalBus.onSystemAlert.emit(SystemAlert(item.text(), AlertType.Event))
        #     else:
        #         signalBus.onSystemAlert.emit(SystemAlert("Invalid Selection Option, see console"))
        #         signalBus.onLogToOutput.emit(f"Expected `Select` option, got {options.action()} instead.")
        # except Exception as e:
        #     signalBus.onSystemAlert.emit(SystemAlert("Invalid Selection Option, see console"))
        #     signalBus.onLogToOutput.emit(f"[Error] {str(e)}")
        pass

    def __handleContextMenuActions(self, options: ProgramExplorerActionModel):
        pass

    # endregion

    # region - workers

    @staticmethod
    def __openTab(tabItem: TabItemModel):
        signalBus.onOpenTab.emit(tabItem)

    # endregion
