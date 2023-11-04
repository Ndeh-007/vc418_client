from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QVBoxLayout, QMainWindow

from controllers.components.menu_bar_controller import MenuBarController
from views.pages.home_page import HomePage
from qframelesswindow import FramelessMainWindow, StandardTitleBar


class MainWindow(FramelessMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__init_ui__()

    def __init_ui__(self):
        """
        initialize the user interface
        :return:
        """
        self.setWindowIcon(QIcon(":resources/images/logo.png"))
        self.setIconSize(QSize(32, 32))

        self.setWindowTitle("VH-418")
        homePage = HomePage()
        self.setCentralWidget(homePage)

        menubar = MenuBarController(None)
        titleBar = StandardTitleBar(self)
        titleBar.setIcon(QIcon(":resources/images/logo.png"))
        # titleBar.setTitle("VH-418")
        self.setTitleBar(titleBar)
        self.titleBar.layout().insertWidget(3, menubar, 0, Qt.AlignmentFlag.AlignLeft)
        self.titleBar.raise_()
