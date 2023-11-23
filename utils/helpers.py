from interfaces.structs import ServerType, ServerState
import store.settings as ss
from utils.signal_bus import signalBus


def changeServerState(serverID: str | ServerType, state: ServerState):
    server = ss.APP_SETTINGS.SERVER.servers(serverID)
    server.setstate(state)
    signalBus.onServerStatusChanged.emit(server)
