import uuid

from PySide6.QtGui import QImage

from controllers.sections.items.program_preview_item_controller import ProgramPreviewItemController
from interfaces.structs import ProgramsExplorerActionType, AlertType, TabUpdateType
from models.explorer.program_item_model import ProgramItemModel
from models.explorer.programs_list_model import ProgramListModel
from models.signal_data_models import ProgramExplorerActionModel, SystemAlert, TabUpdateData
from models.tabs.tab_item_model import TabItemModel
from utils.signal_bus import signalBus
from views.components.dialog.cases.create_new_program import CreateNewProgram
from views.components.dialog.cases.rename_program import CustomRenameProgramDialog
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
        pass

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
        self.programsListView.onError.connect(self.__handleModelError)

    # end region

    # region - Event Handlers

    def __handleListItemDoubleClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        if options.action() == ProgramsExplorerActionType.Open:
            # construct the widget
            w = ProgramPreviewItemController(options)
            t = options.data()[0].text()
            tabModel = TabItemModel(t, w, options.data()[0].id())
            self.__openTab(tabModel)

    def __handleListItemClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        signalBus.onShowProgramProperties.emit(options.data()[0])

    def __handleContextMenuActions(self, options: ProgramExplorerActionModel):
        action = options.action()
        if action == ProgramsExplorerActionType.New:
            self.__newItem()
            return

        # get the data we want to rename or delete
        data = options.data()[0]
        if action == ProgramsExplorerActionType.Rename:
            self.__renameItem(data)
        if action == ProgramsExplorerActionType.Delete:
            self.__deleteItem(data)

    def __handleRenameItemConfirm(self, item: ProgramItemModel | None):
        """
        updates the data inplace in the list view model
        :param item:
        :return:
        """
        if item is None:
            return
        self.model.updateItem(item)
        signalBus.onUpdateTab.emit(TabUpdateData(TabUpdateType.Title, TabItemModel(item.text(), None, item.id())))

    def __handleCreateItemConfirm(self, item: ProgramItemModel | None):
        if item is None:
            return
        # # update the view
        self.model.addItems(item)

        # trigger open of the tab
        data = ProgramExplorerActionModel([item], ProgramsExplorerActionType.Open)
        self.__handleListItemDoubleClicked(data)

    @staticmethod
    def __handleModelError(message: str):
        signalBus.onLogToOutput.emit(message)

    # endregion

    # region - workers

    def __newItem(self):
        """
        creates a new item and opens it in the preview explorer
        :return:
        """
        CreateNewProgram(self, self.__handleCreateItemConfirm)

    def __deleteItem(self, item: ProgramItemModel):
        """
        deletes item from ListView and also signals to delete from the tab if open
        :param item:
        :return:
        """
        self.model.removeItem(item)
        signalBus.onUpdateTab.emit(TabUpdateData(TabUpdateType.Delete, TabItemModel(None, None, item.id())))

    def __renameItem(self, item: ProgramItemModel):
        """
        Renames item.
        Opens a modal collects the response and updates the item's name
        :param item:
        :return:
        """
        CustomRenameProgramDialog(self, item, self.__handleRenameItemConfirm, "Rename", "cancel")

    @staticmethod
    def __openTab(tabItem: TabItemModel):
        signalBus.onOpenTab.emit(tabItem)

    # endregion
