from models.explorer.properties_table_data_model import PropertiesTableDataModel


class ExecutionStepModel:
    def __init__(self,
                 stepType: str = None, priority: int = None, sendTime: int = None, receiveTime: int = None,
                 sourcePid: str = None, targetPid: str = None,
                 message: str = None, action: str = None, data: str = None, index: int = 0):
        self.__stepType: str = stepType
        self.__data: str = str(data)
        self.__priority: int = priority
        self.__sendTime: int = sendTime
        self.__receiveTime: int = receiveTime
        self.__source: str = sourcePid
        self.__target: str = targetPid
        self.__message: str = message
        self.__action: str = action
        self.__propsTableModel: PropertiesTableDataModel = PropertiesTableDataModel({})
        self.__frameIndex: int = index

    # region getters
    def frameIndex(self):
        return self.__frameIndex

    def propsTabelDataModel(self):
        return self.__propsTableModel

    def stepType(self):
        return self.__stepType

    def data(self):
        return self.__data

    def priority(self):
        return self.__priority

    def sendTime(self):
        return self.__sendTime

    def receiveTime(self):
        return self.__receiveTime

    def source(self):
        return self.__source

    def target(self):
        return self.__target

    def message(self):
        return self.__message

    def action(self):
        return self.__action

    # endregion

    # region setters

    def setStepType(self, value: str):
        self.__stepType = value

    def setData(self, value: str):
        self.__data = value

    def setPriority(self, value: int):
        self.__priority = value

    def setSendTime(self, value: int):
        self.__sendTime = value

    def setReceiveTime(self, value: int):
        self.__receiveTime = value

    def setSource(self, value: str):
        self.__source = value

    def setTarget(self, value: str):
        self.__target = value

    def setMessage(self, value: str):
        self.__message = value

    def setAction(self, value: str):
        self.__action = value

    def setPropsTableModel(self, model: PropertiesTableDataModel):
        self.__propsTableModel = model

    # endregion

    # region workers

    def constructPropTableData(self):
        data = {
            "From": self.__source,
            "To": self.__target,
            "Action": self.__action,
            "Data": str(self.__data),
            "Message": self.__message,
        }
        self.__propsTableModel = PropertiesTableDataModel(data, ["Property", "Value"])
    # endregion
