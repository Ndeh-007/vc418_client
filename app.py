import ctypes
import os
import sys

from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from views.main_window import MainWindow

import resources.resources

myAppID = u'ubc.ComplexFluidsGroup.ComplexFluids.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)

basedir = os.path.dirname(__file__)


def main():
    app = QApplication(sys.argv)
    stylePath = os.path.join(basedir, 'styles/app.qss')

    vh418 = MainWindow()

    with open(stylePath, "r") as file:
        vh418.setStyleSheet(file.read())

    vh418.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
