from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt

from models.explorer.properties_table_data_model import PropertiesTableDataModel


class PropertiesTableModel(QAbstractTableModel):
    def __init__(self, data: PropertiesTableDataModel):
        super().__init__()
        self.__propsDataModel = data

    def data(self, index, role=...):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self.__propsDataModel.df().iloc[index.row(), index.column()]
            return str(value)

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

    def rowCount(self, parent=...):
        return self.__propsDataModel.df().shape[0]

    def columnCount(self, parent=...):
        return self.__propsDataModel.df().shape[1]

    def headerData(self, section, orientation, role=...):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.__propsDataModel.df().columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(section + 1)

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

    def clearModel(self):
        self.__propsDataModel.setData({})
        self.__propsDataModel.constructDataFrame()
