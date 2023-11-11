import ctypes
import os
import sys

from PySide6.QtWidgets import QApplication

from views.main_window import MainWindow

import resources.resources
from utils.styling import read_style

myAppID = u'ubc.cpsc.vh418.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)

basedir = os.path.dirname(__file__)


def main():
    app = QApplication(sys.argv)
    stylePath = os.path.join(basedir, 'resources/qss/app.qss')
    vh418 = MainWindow()
    vh418.setStyleSheet(read_style(stylePath))
    vh418.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
