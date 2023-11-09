import qtawesome
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QPushButton

from styles.color import appColors


class AlertBarView(QFrame):
    def __init__(self, showBannerIcon: bool = False):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)

        self.bannerIconWidget = qtawesome.IconWidget()
        ic = qtawesome.icon("msc.info")
        self.bannerIconWidget.setIcon(ic)
        if showBannerIcon:
            layout.addWidget(self.bannerIconWidget)

        self.label = QLabel()
        layout.addWidget(self.label)

        layout.addStretch()

        self.closeButton = QPushButton()
        ic = qtawesome.icon("msc.close", color=appColors.dark_rbg)
        self.closeButton.setIcon(ic)
        self.closeButton.setFlat(True)

        layout.addWidget(self.closeButton)
        self.setLayout(layout)
