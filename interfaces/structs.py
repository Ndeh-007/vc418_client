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


class SystemRequestScope(Enum):
    GLOBAL = 0
    LOCAL = 1


class MenuBarActionType(Enum):
    # file action
    ABOUT = 0
    EXIT = 2
    SETTINGS = 3

    # Server Actions
    START_SERVER = 4
    STOP_SERVER = 5
    LAUNCH_SERVER = 9

    # View actions
    TOGGLE_OUTPUT_EXPLORER = 6
    TOGGLE_PROGRAMS_EXPLORER = 7
    TOGGLE_PROPERTIES_EXPLORER = 8


class PreviewToolbarActionType(Enum):
    FETCH = 0
    EXECUTE = 1
    RELOAD = 2


class BinaryTreeUpdateMode(Enum):
    RELOAD = 0
    RUN = 1


class AnimationPlayerState(Enum):
    OFF = 0
    ON = 1
