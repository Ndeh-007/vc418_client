from enum import Enum


class AlertType(Enum):
    """
    Defines the types of notifications
    """
    Event = "event"
    Error = "error"
    Warning = "warning"
    Success = "success"


class ProgramsExplorerActionType(Enum):
    New = 0
    Delete = 1
    Run = 2
    Select = 3
    Open = 4
