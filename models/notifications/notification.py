from uuid import uuid4

import qtawesome
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


from interfaces.structs import AlertType
from styles.color import appColors


class Notification:
    """
    Creates a notification item.
    """

    def __init__(self, title: str = "", message: str = "",
                 notification_type: AlertType = AlertType.Event):
        self.title = title
        self.message = message
        self.notification_type = notification_type
        self.color = appColors.dark_rbg
        self.icon: QIcon = QIcon()
        self.icon_size = QSize(16, 16)
        self.id = uuid4()
        self.error_name = ""

        # initialize component
        self.initialize()

    def initialize(self):
        """
        Assign the notification color based on the type of event in use
        :return:
        """
        if self.notification_type == AlertType.Event:
            self.color = appColors.tertiary_rbg
            self.icon = qtawesome.icon("msc.info", color=self.color).pixmap(self.icon_size)
            self.error_name = "Event"
        if self.notification_type == AlertType.Warning:
            self.color = appColors.warning_rbg
            self.icon = qtawesome.icon("msc.warning", color=self.color).pixmap(self.icon_size)
            self.error_name = "Warning"
        if self.notification_type == AlertType.Error:
            self.color = appColors.danger_rbg
            self.icon = qtawesome.icon("msc.bug", color=self.color).pixmap(self.icon_size)
            self.error_name = "Error"
