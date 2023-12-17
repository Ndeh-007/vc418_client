from controllers.sections.items.program_preview_item_controller import ProgramPreviewItemController
from interfaces.structs import ProgramsExplorerActionType, TabUpdateType
from models.explorer.program_item_model import ProgramItemModel
from models.explorer.programs_list_model import ProgramListModel
from models.common.signal_data_models import ProgramExplorerActionModel, TabUpdateData
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
        self.connectSignals()

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

    def __handleActiveProgramChanged(self, program: ProgramItemModel):
        pass

    def __handleProgramUpdated(self, program: ProgramItemModel):

        if program is None:
            return
        self.model.updateItem(program)

    def __handleListItemDoubleClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        if options.action() == ProgramsExplorerActionType.Open:
            # construct the widget
            w = ProgramPreviewItemController(options)
            t = options.data()[0].text()
            tabModel = TabItemModel(t, w, options.data()[0].id(), options.data()[0])
            self.__openTab(tabModel)

    def __handleListItemClicked(self, options: ProgramExplorerActionModel):
        """

        :param options:
        :return:
        """
        program = options.data()[0]
        signalBus.onMakeProgramActive.emit(program)
        signalBus.onShowProgramProperties.emit(program)

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
        signalBus.onUpdateTab.emit(TabUpdateData(TabUpdateType.Title, TabItemModel(item.text(), None, item.id(), item)))

        # update the program entry in the store.
        signalBus.onUpdateProgram.emit(item)

    def __handleCreateItemConfirm(self, item: ProgramItemModel | None):
        if item is None:
            return
        # # update the view
        items = self.model.items
        items.append(item)
        self.model = ProgramListModel(items)
        self.programsListView.setModel(self.model)

        # update the store
        signalBus.onCreateProgram.emit(item)

        # trigger open of the tab
        data = ProgramExplorerActionModel([item], ProgramsExplorerActionType.Open)
        self.__handleListItemDoubleClicked(data)

        # trigger open of the properties tab
        signalBus.onShowProgramProperties.emit(item)

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

        items = self.model.items
        index = -1
        for i, itm in enumerate(items):
            if itm.id() == item.id():
                index = i

        if index == -1:
            return

        items.pop(index)
        self.model = ProgramListModel(items)
        self.programsListView.setModel(self.model)

        signalBus.onUpdateTab.emit(TabUpdateData(TabUpdateType.Delete, TabItemModel(None, None, item.id(), item)))

        # remove item from store
        signalBus.onDeleteProgram.emit(item)

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

    # region signals

    def connectSignals(self):
        signalBus.onProgramUpdated.connect(self.__handleProgramUpdated)
        signalBus.onActiveProgramChanged.connect(self.__handleProgramUpdated)
    # endregion
