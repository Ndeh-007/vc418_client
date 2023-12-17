from typing import Callable, Any

from PySide6.QtCore import QTimer, QObject, Signal

from models.notifications.notification import Notification
from models.notifications.notification_manager import NotificationsManager
from views.components.notification_panel import NotificationCardView, NotificationPanelView


class NotificationCardController(NotificationCardView, QObject):
    onDelete = Signal(Notification)

    def __init__(self, data: Notification, deleteHandler: Callable[..., Any] = None, isAlert: bool = None):
        super().__init__(isAlert=isAlert)
        self.data: Notification = data
        self.delete_handler: Callable[..., Any] = deleteHandler
        self.isAlert: bool = isAlert

        # create timer to hide notification
        self.preview_timer = QTimer()
        self.preview_timer.setSingleShot(True)

        self.__initialize()
        self.__configure()

    # region - Initialize
    def __initialize(self):
        self.error_type.setStyleSheet(f"""
            color: {self.data.color};
        """)
        self.error_type.setText(self.data.error_name)
        self.title.setText(self.data.title)
        self.messageArea.setText(self.data.message)

        interval = self.__compute_average_reading_time()
        self.preview_timer.setInterval(interval)

    # endregion

    # region - Configure
    def __configure(self):
        self.close_btn.clicked.connect(self.__deleteNotification)
        self.icon.setPixmap(self.data.icon)

        if self.isAlert:
            self.preview_timer.timeout.connect(self.__deleteNotification)
            self.preview_timer.start()

    # endregion

    # region - Event Handlers
    def __deleteNotification(self):
        if self.delete_handler is not None:
            self.delete_handler(self)
            return
        self.deleteLater()
        self.onDelete.emit(self.data)

    # endregion

    # region - Workers

    def setNotificationData(self, data: Notification):
        self.data = data

    def __compute_average_reading_time(self):
        velocity = 4e-6
        words = len(self.data.title.split()) + len(self.data.message.split())
        return words / velocity
    # endregion


class NotificationPanelController(NotificationPanelView):
    def __init__(self):
        super().__init__()

        self.__manager = NotificationsManager([])

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        pass

    # endregion

    # region - Configure
    def __configure(self):
        self.__manager.onCreate.connect(self.__handleCreateNotification)
        self.__manager.onDelete.connect(self.__handleDeleteNotification)
        self.__manager.onUpdate.connect(self.__handleUpdateNotification)

        self.clearBtn.clicked.connect(self.__clearPanel)
        self.closeBtn.clicked.connect(self.__closePanel)

    # endregion

    # region - Event Handlers

    def __handleUpdateNotification(self, item: list[Notification]):
        pass

    def __handleDeleteNotification(self, item: list[Notification]):
        pass

    def __handleCreateNotification(self, item: list[Notification]):
        pass

    def __closePanel(self):
        self.hide()

    def __clearPanel(self):
        """
        Clears all notifications from the UI and the store
        :return:
        """
        self.clearNotificationItems()

    def __handleRemoveItemSignal(self, item: Notification):
        pass
        # endregion

    # region - Workers
    def updateNotificationItem(self):
        pass

    def clearNotificationItems(self):
        pass

    def __hidePanel(self):
        pass

    def __showPanel(self):
        pass

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass
    # endregion
