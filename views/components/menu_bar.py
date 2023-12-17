from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar

from interfaces.structs import MenuBarActionType


class MenuBarView(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # define the menu bar menus
        fileMenu = self.addMenu("File")
        viewMenu = self.addMenu("View")
        # helpMenu = self.addMenu("Help")

        # region - file menu actions
        launchServerAction = QAction("Start Erlang Server", self)
        aboutAction = QAction("About", self)
        settingsAction = QAction("Settings", self)
        exitAction = QAction("Exit", self)

        launchServerAction.setData(MenuBarActionType.LAUNCH_SERVER)
        aboutAction.setData(MenuBarActionType.ABOUT)
        settingsAction.setData(MenuBarActionType.SETTINGS)
        exitAction.setData(MenuBarActionType.EXIT)

        fileMenu.addActions([launchServerAction, settingsAction, exitAction])
        # endregion

        # region - View menu actions
        self.outputAction = QAction("Output Console", self)
        self.propsAction = QAction("Properties", self)
        self.programAction = QAction("Program", self)

        self.outputAction.setCheckable(True)
        self.propsAction.setCheckable(True)
        self.programAction.setCheckable(True)

        self.outputAction.setData(MenuBarActionType.TOGGLE_OUTPUT_EXPLORER)
        self.propsAction.setData(MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER)
        self.programAction.setData(MenuBarActionType.TOGGLE_PROGRAMS_EXPLORER)

        viewMenu.addActions([self.outputAction, self.propsAction, self.programAction])
        # endregion

        self.setObjectName("MenuBar")
