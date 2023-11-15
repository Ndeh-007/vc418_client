from PySide6.QtCore import QObject, Signal

from models.signal_data_models import SystemAlert, TabUpdateData, SystemRequest
from models.tabs.tab_item_model import TabItemModel


class SignalBus(QObject):
    onServerStatusChanged = Signal(dict)
    onLogToOutput = Signal(str)
    onSystemAlert = Signal(SystemAlert)
    onOpenTab = Signal(TabItemModel)
    onUpdateTab = Signal(TabUpdateData)
    onSystemRequest = Signal(SystemRequest)

    onToggleOutputExplorer = Signal(bool)
    onToggleProgramsExplorer = Signal(bool)
    onTogglePropertiesExplorer = Signal(bool)

    onToggleServer = Signal(bool)
    onOpenSettings = Signal()
    onExitApplication = Signal()


signalBus = SignalBus()
