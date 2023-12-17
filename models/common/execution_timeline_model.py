from models.explorer.properties_table_data_model import PropertiesTableDataModel


class ExecutionTimelineItemModel:
    def __init__(self, index: int, time: int, label: str, value: str):
        self.__index: int = index
        self.__time: int = time
        self.__label: str = label
        self.__value: str = value

    def index(self):
        return self.__index

    def time(self):
        return self.__time

    def label(self):
        return self.__label

    def value(self):
        return self.__value

    def setTime(self, time: int):
        self.__time = time

    def setLabel(self, label: str):
        self.__label = label

    def setIndex(self, index: int):
        self.__index = index

    def setValue(self, value: str):
        self.__value = value


class ExecutionTimelineModel:
    def __init__(self, timelineID: str, data: list[ExecutionTimelineItemModel]):
        self.__data: list[ExecutionTimelineItemModel] = data
        self.__id: str = timelineID
        self.__propsTableModel: PropertiesTableDataModel = PropertiesTableDataModel({})

    def constructTablePropsModel(self, labels: list[str]):
        data = {}
        for item in self.__data:
            data.update({item.label(): item.value()})
        self.__propsTableModel = PropertiesTableDataModel(data, labels)

    def propsTabelDataModel(self):
        return self.__propsTableModel

    def data(self):
        return self.__data

    def dataAtIndex(self, index):
        if index not in range(0, len(self.__data)):
            return -1
        return self.__data[index]

    def id(self):
        return self.__id

    def setPropsTableModel(self, model: PropertiesTableDataModel):
        self.__propsTableModel = model

    def setID(self, timelineId: str):
        self.__id = timelineId

    def setData(self, data: list[ExecutionTimelineItemModel]):
        self.__data = data

    def updateAtIndex(self, index, data):
        self.__data[index] = data
