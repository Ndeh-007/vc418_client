from PySide6.QtCore import QObject, Signal

from models.explorer.program_properties_model import ProgramPropertiesModel
from models.notifications.notification import Notification
from models.settings.http_request_item import HTTPRequestItem
from models.settings.server_model import ServerModel
from models.signal_data_models import SystemAlert, TabUpdateData, SystemRequest
from models.tabs.tab_item_model import TabItemModel


class SignalBus(QObject):
    onServerStatusChanged = Signal(ServerModel)
    onLogToOutput = Signal(str)
    onLogErrorToOutput = Signal(str)

    onSystemAlert = Signal(SystemAlert)
    onSystemNotification = Signal(Notification)
    onSystemProcess = Signal(object)

    onOpenTab = Signal(TabItemModel)
    onUpdateTab = Signal(TabUpdateData)
    onSystemRequest = Signal(SystemRequest)

    onToggleOutputExplorer = Signal(bool)
    onToggleProgramsExplorer = Signal(bool)
    onTogglePropertiesExplorer = Signal(bool)

    onToggleServer = Signal(bool)
    onOpenSettings = Signal()
    onExitApplication = Signal()

    onShowProgramProperties = Signal(ProgramPropertiesModel)
    onHTTPRequest = Signal(HTTPRequestItem)


signalBus = SignalBus()
