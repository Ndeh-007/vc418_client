from PySide6.QtGui import QTextCursor, QFont

from interfaces.structs import MenuBarActionType, SystemRequestScope
from models.common.signal_data_models import SystemRequestData, SystemRequest
from utils.signal_bus import signalBus
from utils.styling import parse_stylesheet_data
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
        font = QFont()
        font.setBold(False)
        self.logger.setFont(font)
        self.logger.setStyleSheet(parse_stylesheet_data("""
                                    QTextEdit#outputTextArea{
                                        border: 0px solid light_shade_rbg;
                                        color: dark_rbg;
                                    }
                                    """))
        self.__updateLogger(message)

    def __handleErrorLogToOutput(self, message: str):
        font = QFont()
        font.setBold(True)
        self.logger.setFont(font)
        self.logger.setStyleSheet(parse_stylesheet_data(""" 
                                    QTextEdit#outputTextArea{
                                        border: 0px solid light_shade_rbg;
                                        color: danger_rbg;
                                    }
                                    """))
        self.__updateLogger(message)

    def __updateLogger(self, msg: str):
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        self.logger.insertPlainText("\n")
        self.logger.insertPlainText(msg)
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
        signalBus.onLogErrorToOutput.connect(self.__handleErrorLogToOutput)
        signalBus.onToggleOutputExplorer.connect(self.__handleOutputToggle)

    # endregion
