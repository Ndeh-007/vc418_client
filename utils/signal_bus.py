from PySide6.QtCore import QObject, Signal

from models.signal_data_models import SystemAlert, TabUpdateData
from models.tabs.tab_item_model import TabItemModel


class SignalBus(QObject):
    onServerStatusChanged = Signal(dict)
    onLogToOutput = Signal(str)
    onSystemAlert = Signal(SystemAlert)
    onOpenTab = Signal(TabItemModel)
    onUpdateTab = Signal(TabUpdateData)


signalBus = SignalBus()
