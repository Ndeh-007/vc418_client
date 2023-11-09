from models.tabs.tab_item_model import TabItemModel
from models.tabs.tab_manager_model import TabManagerModel
from utils.signal_bus import signalBus
from views.sections.preview_explorer import PreviewExplorerView


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

    # region - event handlers

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
        if self.previewTabs.count == 0:
            self.toggleLayout()

    def __handleOpenTab(self, tabItem: TabItemModel):
        """
        Handles all open tabs options.
        If the tab already exists, do not re-initialize, set the tab as the current index
        :param tabItem:
        :return:
        """

        # check if this is the first tab
        if self.previewTabs.count() == 0:
            self.toggleLayout()

        if self.tabManager.tabExists(tabItem):
            self.__makeTabCurrent(tabItem)
        else:
            self.tabManager.addTab(tabItem.id(), tabItem)
            self.previewTabs.setCurrentIndex(self.previewTabs.count() - 1)

    # endregion

    # region - workers

    def __makeTabCurrent(self, tabItem: TabItemModel):
        """
        set tab as the current tab
        :param tabItem:
        :return:
        """
        w = self.tabManager.tabs(tabItem.id())
        i = self.previewTabs.indexOf(w)
        self.previewTabs.setCurrentIndex(i)

    # endregion

    def __connectSignals(self):
        signalBus.onOpenTab.connect(self.__handleOpenTab)
