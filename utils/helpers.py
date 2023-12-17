import json
import re

from PySide6.QtWidgets import QFileDialog

import store.settings as ss
from interfaces.structs import ServerType, ServerState, ProgramType, AlertType
from models.common.execution_step_model import ExecutionStepModel
from models.common.execution_timeline_model import ExecutionTimelineModel, ExecutionTimelineItemModel
from models.common.signal_data_models import TreeStructureModel, TreeStructureItemModel, SystemAlert
from models.graphics.tree_model import BinaryTreeModel
from utils.signal_bus import signalBus


def createSystemErrorAlert(message: str):
    alert = SystemAlert(message, AlertType.Error)
    signalBus.onSystemAlert.emit(alert)


def createSystemEventAlert(message: str):
    alert = SystemAlert(message, AlertType.Event)
    signalBus.onSystemAlert.emit(alert)


def createSystemWarningAlert(message: str):
    alert = SystemAlert(message, AlertType.Warning)
    signalBus.onSystemAlert.emit(alert)


def selectFile(parent):
    """
    Opens a dialog for the user to select a file
    :param parent: the parent widget that calls this function
    :return: the properties of the selected file
    """
    file = QFileDialog.getOpenFileName(parent)[0]
    if len(file) == 0:
        return None
    return file


def selectDirectory():
    """
    Opens a dialog for selecting a folder (directory)
    :return: the properties of the selected directory
    """
    folder = QFileDialog.getExistingDirectory()
    if len(folder) == 0:
        return None
    return folder


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
    if jsonData["program"] == "scam":
        programType = ProgramType.SCAN_ERLANG

    if jsonData["program"] not in ["scan", "reduce"]:
        alert = SystemAlert(
            f"Invalid Program type, got '{jsonData['program']}'. Auto adjusted to 'REDUCE_ERLANG'. Errors may occur.",
            AlertType.Warning)
        signalBus.onSystemAlert.emit(alert)

    # construct frame timelines
    timelines = constructTimelines(ts, jsonData)

    activeProgramFile = ss.APP_SETTINGS.PROGRAMS.activeProgram()
    binaryTree = BinaryTreeModel(jsonData['nprocs'], ts, programType, activeProgramFile)

    # build the frames
    framesArray = []

    frames = jsonData['data']
    i = 0
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
            data=frame['data']['value'],
            index=i
        )
        step.constructPropTableData()
        framesArray.append(step)
        i += 1

    return {
        'executionFrames': framesArray,
        'binaryTree': binaryTree,
        'executionTimelines': timelines
    }


def constructTimelines(tree: TreeStructureModel, jsonData):
    timelines = {}
    frames = jsonData["data"]

    for key in tree.structure().keys():
        arr = []
        index = 0
        frameIndex = 0
        for frame in frames:
            if frame["to"] == key:
                item = ExecutionTimelineItemModel(index, frame['send_time'], f"Frame {frameIndex}",
                                                  str(frame["data"]["step_value"]))
                arr.append(item)
                index += 1
            frameIndex += 1

        timeline = ExecutionTimelineModel(key, arr)
        timeline.constructTablePropsModel(['Frame', "Value"])
        timelines.update({key: timeline})

    return timelines
