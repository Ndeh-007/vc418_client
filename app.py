import ctypes
import sys

from PySide6.QtWidgets import QApplication

from views.main_window import MainWindow

import resources.resources
from utils.styling import q_read_style

myAppID = u'ubc.cpsc.vh418.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)


def main():
    app = QApplication(sys.argv)
    vh418 = MainWindow()
    vh418.terminateApplication.connect(app.quit)
    vh418.setStyleSheet(q_read_style("app"))
    vh418.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
