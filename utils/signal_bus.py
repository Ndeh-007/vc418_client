from PySide6.QtCore import QObject, Signal

from models.explorer.program_item_model import ProgramItemModel
from models.explorer.program_properties_model import ProgramPropertiesModel
from models.graphics.tree_model import BinaryTreeModel
from models.notifications.notification import Notification
from models.settings.http_request_item import HTTPRequestItem
from models.settings.server_model import ServerModel
from models.common.signal_data_models import SystemAlert, TabUpdateData, SystemRequest
from models.tabs.tab_item_model import TabItemModel


class SignalBus(QObject):
    onServerStatusChanged = Signal(ServerModel)
    onLogToOutput = Signal(str)
    onLogErrorToOutput = Signal(str)

    onSystemAlert = Signal(SystemAlert)
    onSystemNotification = Signal(Notification)
    onSystemProcess = Signal(object)
    onTerminateSystemProcess = Signal(str)

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
    onCreateProgram = Signal(ProgramItemModel)
    onUpdateProgram = Signal(ProgramItemModel)
    onDeleteProgram = Signal(ProgramItemModel)
    onMakeProgramActive = Signal(ProgramItemModel)
    onActiveProgramChanged = Signal(ProgramItemModel)
    onProgramUpdated = Signal(ProgramItemModel)

    onHTTPRequest = Signal(HTTPRequestItem)

    onLoadTreeModel = Signal(BinaryTreeModel)
    onUpdateTree = Signal(object)
    onReloadPlayer = Signal()
    onLoadPlayer = Signal(list)

    onSettingsFrameRateChanged = Signal()

    onKillApplication = Signal()


signalBus = SignalBus()
