from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton

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
        self.hide()

    def __handleLogToOutput(self, message: str):
        self.logger.moveCursor(QTextCursor.MoveOperation.End)
        self.logger.insertPlainText("\n")
        self.logger.insertPlainText(message)
        sb = self.logger.verticalScrollBar()
        sb.setValue(sb.maximum())

    # endregion

    def __connectSignals(self):
        signalBus.onLogToOutput.connect(self.__handleLogToOutput)
