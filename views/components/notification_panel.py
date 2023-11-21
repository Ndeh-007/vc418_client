import qtawesome
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QGraphicsDropShadowEffect, QLabel, QHBoxLayout, \
    QScrollArea, QWidget

from utils.styling import setPaletteColor
from views.components.section_header import SectionHeader

from styles.color import appColors, appColorsRBG


class NotificationCardView(QFrame):
    def __init__(self, isAlert: bool = False):
        super().__init__()
        # define layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # region header
        header = QFrame()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(5, 0, 5, 0)

        self.icon = QLabel()

        header_layout.addWidget(self.icon)

        self.error_type = QLabel()
        header_layout.addWidget(self.error_type)

        header_layout.addStretch()

        self.close_btn = QPushButton()
        close_icon = qtawesome.icon("msc.close", color=appColors.medium_shade_rbg)
        self.close_btn.setIcon(close_icon)
        self.close_btn.setFlat(True)

        header_layout.addWidget(self.close_btn)

        header.setLayout(header_layout)
        layout.addWidget(header)
        # endregion

        # region body
        body = QFrame()
        body_layout = QVBoxLayout()
        body_layout.setContentsMargins(25, 5, 10, 10)

        self.title = QLabel()
        self.title.setStyleSheet(f"""
            font-weight: bold;
            font-size: 14px;
            color: {appColors.dark_rbg}
        """)
        body_layout.addWidget(self.title)

        self.messageArea = QLabel()
        self.messageArea.setWordWrap(True)
        self.messageArea.setStyleSheet(f""" 
            color: {appColors.dark_tint_rbg}
        """)

        body_layout.addWidget(self.messageArea)

        body.setLayout(body_layout)

        layout.addWidget(body)
        # endregion

        layout.setSpacing(0)
        # layout.addStretch()
        self.setLayout(layout)
        setPaletteColor(self, "white")

        # add drop shadow if we are using an alert
        if isAlert:

            effect = QGraphicsDropShadowEffect(self, enabled=True)
            effect.setColor(appColorsRBG.dark_tint_rbg)
            effect.setOffset(0, 0)
            effect.setBlurRadius(5)
            self.setGraphicsEffect(effect)
            setPaletteColor(self, appColorsRBG.light_rbg)


class NotificationPreviewView(QFrame):
    def __init__(self):
        super().__init__()


class NotificationPanelView(QFrame):
    def __init__(self):
        super().__init__()

        # define ui

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # region header

        # region - Header control buttons
        self.closeBtn = QPushButton()
        ic = qtawesome.icon("msc.close", color=appColors.dark_rbg)
        self.closeBtn.setIcon(ic)
        self.closeBtn.setFlat(True)

        self.clearBtn = QPushButton()
        ic = qtawesome.icon("msc.clear-all", color=appColors.dark_rbg)
        self.clearBtn.setIcon(ic)
        self.clearBtn.setFlat(True)

        controlButtons = [self.clearBtn, self.closeBtn]

        # endregion

        header = SectionHeader("Notifications", control_buttons=controlButtons)
        layout.addWidget(header)

        # endregion

        # region body
        body_scroll_area = QScrollArea()
        body_scroll_area.setFrameStyle(QFrame.Shape.NoFrame)
        body_scroll_area.setContentsMargins(0, 0, 0, 0)

        body_scroll_area_widget = QWidget()
        self.body_scroll_area_widget_layout = QVBoxLayout()
        self.body_scroll_area_widget_layout.setContentsMargins(0, 0, 0, 0)

        # region body content goes here
        content_widget = QFrame()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        content_widget.setLayout(self.content_layout)
        self.body_scroll_area_widget_layout.addWidget(content_widget)
        # endregion body content end

        self.body_scroll_area_widget_layout.addStretch()
        body_scroll_area_widget.setLayout(self.body_scroll_area_widget_layout)
        setPaletteColor(body_scroll_area_widget, appColors.light_rbg)

        body_scroll_area.setWidgetResizable(True)
        body_scroll_area.setWidget(body_scroll_area_widget)

        layout.addWidget(body_scroll_area)

        self.setLayout(layout)

        # endregion
