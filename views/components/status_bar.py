from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QStatusBar


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
        btn1ContentLayout = QHBoxLayout()
        # btn1ContentLayout.setContentsMargins(0, 0, 0, 0)
        erlangServerLabel = QLabel("Erlang Server")
        self.erlangServerStatus = QLabel("off")
        btn1ContentLayout.addWidget(erlangServerLabel)
        btn1ContentLayout.addWidget(self.erlangServerStatus)
        btn1Content.setLayout(btn1ContentLayout)

        self.erlangServerBtn = StatusBarViewButton(btn1Content)
        layout.addWidget(self.erlangServerBtn)

        btn2Content = QFrame()
        btn2ContentLayout = QHBoxLayout()
        # btn2ContentLayout.setContentsMargins(0, 0, 0, 0)
        cppServerLabel = QLabel("C++ Server")
        self.cppServerStatus = QLabel("off")
        btn2ContentLayout.addWidget(cppServerLabel)
        btn2ContentLayout.addWidget(self.cppServerStatus)
        btn2Content.setLayout(btn2ContentLayout)

        self.cppServerBtn = StatusBarViewButton(btn2Content)
        layout.addWidget(self.cppServerBtn)

        w = QWidget()
        w.setLayout(layout)

        self.addWidget(btn1Content)
        self.addWidget(btn2Content)

        self.setSizeGripEnabled(False)
