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
    Rename = 6


class TabUpdateType(Enum):
    Title = 0
    Delete = 1


class ProgramType(Enum):
    UNDEFINED = 0
    REDUCE_ERLANG = 1
    SCAN_ERLANG = 2


class ServerType(Enum):
    UNDEFINED = 0
    ERLANG = 1
    C_PLUS_PLUS = 2


class ServerState(Enum):
    ON = 0
    OFF = 1
    WORKING = 2
    TRANSITION = 3
