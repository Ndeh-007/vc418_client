from typing import Literal

from PySide6.QtCore import QObject, Signal

from models.notifications.notification import Notification
from utils.signal_bus import signalBus


class NotificationsManager(QObject):
    """
    Class to hold all system notifications.
    notifications are stored with the most recent ones first.
    """

    onCreate = Signal(list[Notification])
    onDelete = Signal(list[Notification])
    onUpdate = Signal(list[Notification])
    onDataChanged = Signal(list[Notification])

    def __init__(self, notifications: list[Notification]):
        super().__init__()
        """
        Initialize the class
        :param notifications: start up notifications
        """
        self.__notifications: list[Notification] = notifications

        self.connect_signals()

        self.__handle_notification_data_changes__("set", notifications)

    def clear_notifications(self):
        """
        remove all notifications from the system
        :return:
        """
        self.__notifications = []
        self.onDataChanged.emit(self.__notifications)

    def addNotifications(self, items: list[Notification] | Notification):
        """
        add a notification to the list of notifications.
        item is added to the front. most recent items comes first
        :param items: the item to be added
        :return:
        """
        arr = []
        if isinstance(items, list):
            arr += items
        else:
            arr.append(items)

        for item in arr:
            self.__notifications.insert(0, item)
        self.__handle_notification_data_changes__(action="add", data=arr)

    def __get_notification(self, notification_id: str):
        """
        return notification at position provided.
        :param notification_id: notification id.
        :return: the notifications at provided id
        """
        for item in self.__notifications:
            if item.id == notification_id:
                return item

    def notifications(self, notification_id: str = None):
        """
        gets all notifications. or a target notification by the ID
        :return: all  notifications.
        """
        if notification_id:
            return self.__get_notification(notification_id)
        return self.__notifications

    # this function may not be used in the future
    def updateNotification(self, index: int, item: Notification):
        """
        Changes the value of a notification at position with the required data
        :param index: position in list
        :param item: the new notification
        :return:
        """
        self.__notifications[index] = item
        self.__handle_notification_data_changes__(action="update", data=[item])

    def setNotifications(self, items: list[Notification]):
        """
        reset the notifications with a new value
        :param items: the list of notifications
        :return:
        """
        self.__notifications = items
        self.__handle_notification_data_changes__(action="set", data=items)

    def deleteNotification(self, notification: Notification):
        """
        remove a particular notification
        :param notification: the notifications to be removed
        :return:
        """
        index = 0
        for item in self.__notifications:
            if item.id == notification.id:
                break
            index = index + 1
        item = None
        if index in range(len(self.__notifications)):
            item = self.__notifications.pop(index)
        self.__handle_notification_data_changes__(action="delete", data=item)

    def purify_notifications(self):
        """
        Removes all duplicating notifications
        :return:
        """
        notif_set = set(self.__notifications)
        self.__notifications = list(notif_set)

    def __handle_notification_data_changes__(self, action: Literal['add', 'set', 'delete', 'update', 'clear'], data: list[Notification] | Notification):
        """
        Signal the UI that a change has occurred in the list of notifications
        :return:
        """
        if action == "add":
            self.onCreate.emit(data)
        if action == "set":
            self.onCreate.emit(data)
        if action == "delete":
            self.onDelete.emit(data)
        if action == "update":
            self.onUpdate.emit(data)
        if action == "clear":
            self.onCreate.emit(data)

        self.onDataChanged.emit()

    def connect_signals(self):
        signalBus.onSystemNotification.connect(self.addNotifications)
