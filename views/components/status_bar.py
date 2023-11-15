import qtawesome
from PySide6.QtCore import QSize, QObject, Signal
from PySide6.QtGui import QMouseEvent, Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QWidget, QLabel, QStatusBar, QGridLayout

from styles.color import appColors


class StatusBarViewButton(QFrame, QObject):
    clicked = Signal()

    def __init__(self, content: QWidget, cMargin: int | list[int] = 0):
        super().__init__()
        layout = QVBoxLayout()

        if isinstance(cMargin, int):
            cMargin = [cMargin, cMargin, cMargin, cMargin]

        layout.setContentsMargins(cMargin[0], cMargin[1], cMargin[2], cMargin[3])
        layout.addWidget(content)
        self.setLayout(layout)
        self.setObjectName("StatusBarViewButton")

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()


class StatusBarView(QStatusBar):
    def __init__(self):
        super().__init__()

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

        self.addWidget(self.erlangServerBtn, 0)
        self.addWidget(QWidget(), 1)

        self.outputBtn = StatusBarViewButton(QLabel("Output"), 2)
        self.notificationBtn = StatusBarViewButton(qtawesome.IconWidget("msc.bell", color=appColors.medium_rbg), 2)

        self.addWidget(self.outputBtn, 0)
        self.addWidget(self.notificationBtn, 0)

        self.setSizeGripEnabled(False)
