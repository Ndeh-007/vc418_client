from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

from controllers.components.menu_bar_controller import MenuBarController
from controllers.components.status_bar_controller import StatusBarController
from controllers.pages.HomePageController import HomePageController
from store.settings import init_settings_store
from utils.signal_bus import signalBus


class MainWindow(QMainWindow, QObject):
    terminateApplication = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        init_settings_store()
        self.__init_ui__(parent)
        self.connectSignals()

    def __init_ui__(self, parent):
        """
        initialize the user interface
        :return:
        """
        self.setWindowIcon(QIcon(":resources/images/logo.png"))

        self.setWindowTitle("VH-418")

        menubar = MenuBarController()
        self.setMenuBar(menubar)

        homePage = HomePageController(parent)
        self.setCentralWidget(homePage)

        statusBar = StatusBarController()
        self.setStatusBar(statusBar)

        self.resize(1080, 800)

    def __handleKillApplication(self):
        self.terminateApplication.emit()

    def connectSignals(self):
        signalBus.onKillApplication.connect(self.__handleKillApplication)
