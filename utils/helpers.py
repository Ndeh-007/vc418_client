import json
import re

from interfaces.structs import ServerType, ServerState, ProgramType, AlertType
import store.settings as ss
from models.common.execution_step_model import ExecutionStepModel
from models.common.signal_data_models import TreeStructureModel, TreeStructureItemModel, SystemAlert
from models.graphics.tree_model import BinaryTreeModel
from utils.signal_bus import signalBus


def changeServerState(serverID: str | ServerType, state: ServerState):
    server = ss.APP_SETTINGS.SERVER.servers(serverID)
    server.setstate(state)
    signalBus.onServerStatusChanged.emit(server)


def getPidNumber(pid: str):
    """
    takes an input of the format "<0.xxx.0>" and extracts the value of xxx
    :param pid:
    :return:
    """
    pattern = r"<(\d+)\.\d+\.\d+>"  # Regex pattern to match the number within the angle brackets
    match = re.search(pattern, pid)
    if match:
        return int(match.group(1))
    else:
        return None


def parseJSONData(filePath: str):
    """
    parses data from the provided json file
    :param filePath:
    :return:
    """

    # first read data from the file
    with open(filePath, 'r') as file:
        jsonData = json.load(file)

    # build the tree
    struct = {}
    rootPid = None

    tree = jsonData['tree']
    for item in tree:
        if item['parent'] is None:
            rootPid = item['self']
        tsi = TreeStructureItemModel(
            item['self'],
            item['parent'],
            item['children']
        )
        struct.update({item['self']: tsi})
    ts = TreeStructureModel(rootPid, struct)

    #  CHECK_ME: check the program type (this maybe irrelevant, still unsure)
    program = ProgramType.REDUCE_ERLANG
    if jsonData["program"] == "scan":
        program = ProgramType.SCAN_ERLANG
    else:
        alert = SystemAlert(f"Invalid Program type, got {jsonData['program']}. Auto adjusted to 'REDUCE_ERLANG'", AlertType.Warning)
        signalBus.onSystemAlert.emit(alert)
    binaryTree = BinaryTreeModel(jsonData['nprocs'], ts, program)

    # build the frames
    framesArray = []

    frames = jsonData['data']
    for frame in frames:
        step = ExecutionStepModel(
            stepType=frame['type'],
            priority=frame['priority'],
            sendTime=frame['send_time'],
            receiveTime=frame['receive_time'],
            sourcePid=frame['from'],
            targetPid=frame['to'],
            message=frame['msg'],
            action=frame['data']['action'],
            data=frame['data']['value']
        )
        framesArray.append(step)

    return {
        'executionFrames': framesArray,
        'binaryTree': binaryTree
    }
