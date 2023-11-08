from enum import Enum


class AlertType(Enum):
    """
    Defines the types of notifications
    """
    Event = "event"
    Error = "error"
    Warning = "warning"
    Success = "success"
