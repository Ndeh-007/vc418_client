from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from controllers.components.menu_bar_controller import MenuBarController
from controllers.components.status_bar_controller import StatusBarController
from controllers.pages.HomePageController import HomePageController


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__init_ui__(parent)

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
