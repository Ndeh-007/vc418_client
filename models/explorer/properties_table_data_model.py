import pandas as pd


class PropertiesTableDataModel:
    def __init__(self, data: dict[str, str], label: list[str] = None):
        self.__data = data
        self.__df: pd.DataFrame = pd.DataFrame([])
        self.__labels: list[str] = label
        if label is None:
            self.__labels: list[str] = ['Label', 'Value']

        self.constructDataFrame()

    def constructDataFrame(self):
        arr = []
        for key in self.__data.keys():
            arr.append([key, self.__data.get(key)])

        self.__df = pd.DataFrame(arr, columns=self.__labels)
        return self.__df

    def df(self):
        return self.__df

    def labels(self):
        return self.__labels

    def update(self, target, data):
        self.__data.update({target: data})

    def data(self, target: str = None):
        if target is not None:
            return self.__data.get(target)
        return self.__data

    def setData(self, data: dict[str, str]):
        self.__data = data

    def setLabels(self, labels: list[str]):
        self.__labels = labels
