from collections.abc import Callable
from typing import Any

from PySide6.QtCore import QThread, QObject, Signal

from models.common.signal_data_models import SystemAlert
from utils.signal_bus import signalBus


class ThreadDataModel:
    def __init__(self, message: str | None, action: Callable[..., Any] | None, p_id: str):
        self.message = message
        self.action = action
        self.threadID = p_id
        self.data = None


class ProcessItem:
    """
    Defines the item to be passed around. Carries details about what is going to be performed on the different threads
    """

    def __init__(self, itemID: str, task: Callable[..., Any], args: Any = None,
                 onCompleteTask: Callable[..., Any] = None,
                 onErrorTask: Callable[..., Any] = None,
                 onStartTask: Callable[..., Any] = None
                 ):
        self.__id = itemID
        self.__task = task
        self.__args = args
        self.__onCompleteTask = onCompleteTask
        self.__onErrorTask = onErrorTask
        self.__onStartTask = onStartTask

    def onErrorTask(self):
        return self.__onErrorTask

    def onStartTask(self):
        return self.__onStartTask

    def onCompleteTask(self):
        return self.__onCompleteTask

    def id(self):
        return self.__id

    def task(self):
        return self.__task

    def args(self):
        return self.__args

    def execute(self):
        if self.__args is not None:
            return self.__task(self.__args)
        else:
            return self.__task()


class ProcessThread(QThread, QObject):
    """
    subclasses Qthread. executes the task provided by the process item
    """
    onExecutionComplete = Signal(ThreadDataModel)
    onExecutionError = Signal(ThreadDataModel)
    onExecutionStarted = Signal(ThreadDataModel)

    def __init__(self, item: ProcessItem):
        super().__init__()
        self.__threadId = item.id()
        self.__processItem = item

        self.__executionResults: ThreadDataModel = ThreadDataModel(None, None, self.__threadId)
        self.__executionError: ThreadDataModel = ThreadDataModel(None, None, self.__threadId)
        self.__executionStarted: ThreadDataModel = ThreadDataModel(None, None, self.__threadId)

        # initialize
        self.__executionStarted.action = self.__processItem.onStartTask()
        self.__executionResults.action = self.__processItem.onCompleteTask()
        self.__executionError.action = self.__processItem.onErrorTask()

        # configure
        self.finished.connect(self.__handleThreadFinished)
        self.started.connect(self.__handleThreadStarted)

    def threadID(self):
        return self.__threadId

    def processItem(self):
        return self.__processItem

    def __handleThreadFinished(self):
        self.onExecutionComplete.emit(self.__executionResults)

    def __handleThreadStarted(self):
        self.onExecutionStarted.emit(self.__executionStarted)

    def run(self):
        try:
            results = self.__processItem.execute()
            self.__executionResults.message = "Process Complete"
            self.__executionResults.data = results
        except Exception as e:
            self.__executionError.message = str(e)
            self.onExecutionError.emit(self.__executionError)


class ProcessManager(QObject):
    """
    manages the threads
    """

    def __init__(self):
        super().__init__()

        self.__threads: dict[str, ProcessThread] = {}

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        pass

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers
    def __handleNewSubProcess(self, processItem: ProcessItem):
        """
        creates and executes a thread with the data in the process item
        :param processItem:
        :return:
        """

        # define thread
        t = ProcessThread(processItem)

        # configure thread actions
        t.onExecutionComplete.connect(self.__handleThreadComplete)
        t.onExecutionError.connect(self.__handleThreadError)
        t.onExecutionStarted.connect(self.__handleExecutionStarted)

        # add to thread dictionary
        self.__threads.update({t.threadID(): t})

        # execute thread
        t.start()

    @staticmethod
    def __handleExecutionStarted(info: ThreadDataModel):
        if info.action is None:
            return

        info.action()

    @staticmethod
    def __handleThreadComplete(result: ThreadDataModel):
        if result.action is None:
            return
        # pass the results of the execution as a parameter
        # for the onComplete action.
        result.action(result.data)

    @staticmethod
    def __handleThreadError(error: ThreadDataModel):
        if error.action is None:
            alert = SystemAlert(error.message)
            signalBus.onSystemAlert.emit(alert)
            return

        error.action()

    # endregion

    # region - Workers
    def terminateThread(self, target: str):
        """
        removes a thread from the list of threads and kills it
        :param target:
        :return:
        """
        t = self.__threads.get(target)

        if t is None:
            return
        self.__threads.pop(target)
        t.terminate()
        t.wait()
    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        signalBus.onSystemProcess.connect(self.__handleNewSubProcess)
        signalBus.onTerminateSystemProcess.connect(self.terminateThread)

    # endregion

    # region - Getters
    def threads(self):
        return self.__threads

    # endregion

    # region - Setters

    # endregion
