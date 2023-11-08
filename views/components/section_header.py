import qtawesome
from PySide6.QtWidgets import QLabel, QHBoxLayout, QFrame, QPushButton, QToolBar, QWidget

from styles.color import appColors


class SectionHeader(QFrame):
    """
    Defines the header of a section in the main application layout
    """

    def __init__(self, title: str, control_buttons: list[QWidget] = None):
        super(SectionHeader, self).__init__()
        header_label = IconLabel("msc.gripper", title, appColors.medium_tint_rbg)
        header_label.setContentsMargins(0, 0, 0, 0)
        header_layout = QHBoxLayout()
        header_layout.addWidget(header_label)
        header_layout.addStretch()
        toolbar = SectionHeaderToolbar(control_buttons)
        header_layout.addWidget(toolbar)
        header_layout.setContentsMargins(0, 0, 0, 0)

        self.setObjectName("SectionHeader")
        self.setLayout(header_layout)


class IconLabel(QToolBar):
    """
    Defines the label title alongside with an icon. This is the label used in the section header.
    """

    def __init__(self, qta_id, text, icon_color: str):
        super(IconLabel, self).__init__()
        button = QPushButton()
        button.setFlat(True)
        button.setDisabled(True)
        btn_icon = qtawesome.icon(qta_id, color=icon_color)
        button.setIcon(btn_icon)

        label = QLabel(text)
        label.setObjectName("SectionHeaderLabel")

        self.addWidget(button)
        self.addWidget(label)


class SectionHeaderToolbar(QToolBar):
    """
    Creates a toolbar to hold the buttons that can be added to the section header
    """

    def __init__(self, control_buttons: list[QPushButton] = None):
        super().__init__()
        dummy_button = QPushButton()
        dummy_button.setDisabled(True)
        dummy_button.setFlat(True)

        buttons = control_buttons
        if control_buttons is None:
            buttons = [dummy_button]

        for button in buttons:
            self.addWidget(button)
