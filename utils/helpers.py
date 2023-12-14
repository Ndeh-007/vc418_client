import json
import re
import time

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


def isFalsePid(pid: str):
    pattern = r"{<0\.(\d+)\.\d+>}"
    match = re.search(pattern, pid)
    if match:
        return True
    else:
        return False


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
    items = []
    rootPid = None

    tree = jsonData['tree']
    for item in tree:

        if isFalsePid(item['parent']):
            parent = None
        else:
            parent = item['parent']

        if parent is None:
            rootPid = item['self']
        tsi = TreeStructureItemModel(
            item['self'],
            parent,
            item['children'],
            item['value'],
            item['index']
        )
        items.append(tsi)
    # sort them according to their index
    items.sort(key=lambda x: x.index())
    for item in items:
        struct.update({item.id(): item})
    ts = TreeStructureModel(rootPid, struct)

    #  CHECK_ME: check the program type (this maybe irrelevant, still unsure)
    programType = ProgramType.REDUCE_ERLANG
    if jsonData["program"] == "scan":
        programType = ProgramType.SCAN_ERLANG
    else:
        alert = SystemAlert(f"Invalid Program type, got {jsonData['program']}. Auto adjusted to 'REDUCE_ERLANG'",
                            AlertType.Warning)
        signalBus.onSystemAlert.emit(alert)
    activeProgramFile = ss.APP_SETTINGS.PROGRAMS.activeProgram()
    # print("active program in json parser", activeProgramFile)
    # time.sleep(0.5)
    binaryTree = BinaryTreeModel(jsonData['nprocs'], ts, programType, activeProgramFile)
    # binaryTree.setProgramItem(activeProgramFile)

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
