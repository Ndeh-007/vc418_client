from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton

from interfaces.structs import MenuBarActionType, SystemRequestScope
from models.signal_data_models import SystemRequestData, SystemRequest
from utils.signal_bus import signalBus
from views.components.section_header import SectionHeader
from views.sections.output_explorer import OutputExplorerView


class OutputExplorerController(OutputExplorerView):
    def __init__(self):
        super().__init__()

        self.configure()

        self.__connectSignals()

    # region configure

    def configure(self):
        self.clearBtn.clicked.connect(self.__handleClear)
        self.minimizeBtn.clicked.connect(self.__handleMinimize)

    # endregion

    # region - event handlers
    def __handleClear(self):
        self.logger.clear()

    def __handleMinimize(self):
        d = SystemRequestData(MenuBarActionType.TOGGLE_OUTPUT_EXPLORER, MenuBarActionType.TOGGLE_OUTPUT_EXPLORER)
        self.__fireSystemRequest(d)

    def __handleLogToOutput(self, message: str):
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        self.logger.insertPlainText("\n")
        self.logger.insertPlainText(message)
        sb = self.logger.verticalScrollBar()
        sb.setValue(sb.maximum())

    def __handleOutputToggle(self, state: bool):
        self.setHidden(not state)

    # endregion

    # region - Workers
    @staticmethod
    def __fireSystemRequest(data: SystemRequestData, scope: SystemRequestScope = None):
        if scope:
            request = SystemRequest(data, scope)
        else:
            request = SystemRequest(data)
        signalBus.onSystemRequest.emit(request)

    # endregion

    # region - Signals
    def __connectSignals(self):
        signalBus.onLogToOutput.connect(self.__handleLogToOutput)
        signalBus.onToggleOutputExplorer.connect(self.__handleOutputToggle)

    # endregion
