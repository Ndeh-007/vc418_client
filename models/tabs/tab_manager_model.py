from models.tabs.tab_item_model import TabItemModel


class TabManagerModel:
    def __init__(self, tabs: dict[str, TabItemModel]):
        self.__tabs = tabs

    # region - getters
    def tabs(self, target: str = None):
        if target:
            return self.__tabs.get(target)
        return self.__tabs

    # endregion

    # region - setters

    def setTabs(self, tabs: dict[str, TabItemModel]):
        self.__tabs = tabs

    # endregion

    # region - workers
    def clear(self):
        self.__tabs.clear()

    def addTab(self, target: str, data: TabItemModel):
        self.__tabs.update({target: data})

    def deleteTab(self, target: str):
        return self.__tabs.pop(target)

    def tabExists(self, tabItem: TabItemModel):
        if tabItem.id() in self.__tabs.keys():
            return True
        else:
            return False

    def getTabWithTitle(self, title: str):
        """
        returns the item whose title matches the provided title. or None if it does not exist
        :param title:
        :return:
        """
        for key in self.__tabs.keys():
            item = self.__tabs.get(key)
            if title == item.title():
                return item
        return None

    # endregion
