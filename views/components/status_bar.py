import qtawesome
from PySide6.QtCore import QSize, QSize
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QStatusBar, QGridLayout


class StatusBarViewButton(QPushButton):
    def __init__(self, content: QWidget):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(content)
        self.setLayout(layout)
        self.setFlat(True)


class StatusBarView(QStatusBar):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 5, 0, 5)

        btn1Content = QFrame()
        btn1ContentLayout = QGridLayout()
        btn1ContentLayout.setContentsMargins(2, 2, 2, 2)
        btn1ContentLayout.setVerticalSpacing(0)
        btn1ContentLayout.setHorizontalSpacing(5)
        erlangServerLabel = QLabel("Erlang")
        self.erlangServerIndicator = qtawesome.IconWidget()
        self.erlangServerIndicator.setIconSize(QSize(10, 10))
        self.erlangServerStatus = QLabel()
        self.erlangServerStatus.setObjectName("ServerStatusLabel")
        btn1ContentLayout.addWidget(self.erlangServerIndicator, 0, 0)
        btn1ContentLayout.addWidget(erlangServerLabel, 0, 1)
        btn1ContentLayout.addWidget(self.erlangServerStatus, 1, 1, 1, 2)
        btn1Content.setLayout(btn1ContentLayout)

        self.erlangServerBtn = StatusBarViewButton(btn1Content)
        layout.addWidget(self.erlangServerBtn)

        btn2Content = QFrame()
        btn2ContentLayout = QGridLayout()
        btn2ContentLayout.setContentsMargins(2, 2, 2, 2)
        btn2ContentLayout.setVerticalSpacing(0)
        btn2ContentLayout.setHorizontalSpacing(5)
        cppServerLabel = QLabel("C++")
        self.cppServerIndicator = qtawesome.IconWidget()
        self.cppServerIndicator.setIconSize(QSize(10, 10))
        self.cppServerStatus = QLabel()
        self.cppServerStatus.setObjectName("ServerStatusLabel")
        btn2ContentLayout.addWidget(self.cppServerIndicator, 0, 0)
        btn2ContentLayout.addWidget(cppServerLabel, 0, 1)
        btn2ContentLayout.addWidget(self.cppServerStatus, 1, 1, 1, 2)
        btn2Content.setLayout(btn2ContentLayout)

        self.cppServerBtn = StatusBarViewButton(btn2Content)
        layout.addWidget(self.cppServerBtn)

        w = QWidget()
        w.setLayout(layout)

        self.addWidget(btn1Content)
        self.addWidget(btn2Content)

        self.setSizeGripEnabled(False)
