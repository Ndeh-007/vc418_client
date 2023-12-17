from interfaces.structs import TabUpdateType
from models.common.signal_data_models import TabUpdateData
from models.tabs.tab_item_model import TabItemModel
from models.tabs.tab_manager_model import TabManagerModel
from utils.signal_bus import signalBus
from views.sections.preview_explorer import PreviewExplorerView
import store.settings as ss


class PreviewExplorerController(PreviewExplorerView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabManager = TabManagerModel({})
        self.explorerLayout.setCurrentIndex(0)

        self.initialize()
        self.configure()
        self.__connectSignals()

    def initialize(self):
        pass

    def configure(self):
        self.previewTabs.tabCloseRequested.connect(self.__handleTabCloseRequest)
        self.previewTabs.tabBarClicked.connect(self.__handleTabClicked)

    # region - event handlers

    def __handleTabClicked(self, index: int):
        """
        when user clicks, make the current tab the active tab
        :param index:
        :return:
        """
        title = self.previewTabs.tabText(index)
        item = self.tabManager.getTabWithTitle(title)
        ss.APP_SETTINGS.PROGRAMS.makeProgramWithIdActive(item.program().id())
        program = ss.APP_SETTINGS.PROGRAMS.programs(item.program().id())
        signalBus.onShowProgramProperties.emit(program)

    def __handleTabCloseRequest(self, index: int):
        """
        closes tab and removes it from the manager
        :param index:
        :return:
        """
        title = self.previewTabs.tabText(index)
        item = self.tabManager.getTabWithTitle(title)
        if item is not None:
            self.tabManager.deleteTab(item.id())
        self.previewTabs.removeTab(index)

        # if the last tab was removed
        if self.previewTabs.count() < 1:
            self.toggleLayout()

    def __handleOpenTab(self, tabItem: TabItemModel):
        """
        Handles all open tabs options.
        If the tab already exists, do not re-initialize, set the tab as the current index
        :param tabItem:
        :return:
        """

        # check if this is the first tab
        if self.previewTabs.count() < 1:
            self.toggleLayout()

        if self.tabManager.tabExists(tabItem):
            self.__makeTabCurrent(tabItem)
        else:
            self.tabManager.addTab(tabItem.id(), tabItem)
            self.previewTabs.addTab(tabItem.content(), tabItem.title())
            self.previewTabs.setCurrentIndex(self.previewTabs.count() - 1)

    def __handleUpdateTab(self, options: TabUpdateData):
        """
        updates tab based on the update type
        :param options:
        :return:
        """
        updateType = options.updateType()
        data = options.data()
        if updateType == TabUpdateType.Title:
            self.__updateTabTitle(data)

        if updateType == TabUpdateType.Delete:
            self.__deleteTab(data)

    # endregion

    # region - workers
    def __deleteTab(self, data: TabItemModel):

        # first check if the tab has been created
        if not self.tabManager.tabExists(data.id()):
            return

        i = self.tabManager.getTabIndex(data.id())
        self.tabManager.deleteTab(data.id())
        self.previewTabs.removeTab(i)

        if self.previewTabs.count() < 1:
            self.toggleLayout()

    def __updateTabTitle(self, data: TabItemModel):

        # first check if the tab has been created
        if not self.tabManager.tabExists(data.id()):
            return

        i = self.tabManager.getTabIndex(data.id())
        self.tabManager.tabs(data.id()).setTitle(data.title())
        self.previewTabs.setTabText(i, data.title())

    def toggleLayout(self):
        """
        switches the layout between showing the tabs and the placeholder
        :return:
        """
        if self.explorerLayout.currentIndex() == 0:
            self.explorerLayout.setCurrentIndex(1)
        else:
            self.explorerLayout.setCurrentIndex(0)

    def __makeTabCurrent(self, tabItem: TabItemModel):
        """
        set tab as the current tab
        :param tabItem:
        :return:
        """
        i = self.tabManager.getTabIndex(tabItem.id())
        self.previewTabs.setCurrentIndex(i)

    # endregion

    def __connectSignals(self):
        signalBus.onOpenTab.connect(self.__handleOpenTab)
        signalBus.onUpdateTab.connect(self.__handleUpdateTab)
