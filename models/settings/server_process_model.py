from PySide6.QtCore import QObject, Signal, QProcess

from models.settings.server_model import ServerModel
from models.common.signal_data_models import SystemAlert
from utils.signal_bus import signalBus


class ServerProcessModel(QObject):
    onLaunchSuccessful = Signal(ServerModel)
    onLaunchFailed = Signal(ServerModel)
    onKill = Signal(ServerModel)

    def __init__(self, server: ServerModel, command: str, arguments: list[str]):
        super().__init__()
        self.__server: ServerModel = server
        self.__process: QProcess = QProcess()

        self.__arguments: list[str] = arguments
        self.__command: str = command

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        self.__process.setWorkingDirectory(self.arguments()[0])

    # endregion

    # region - Configure
    def __configure(self):
        self.__process.errorOccurred.connect(self.__handleErrorOccurred)
        self.__process.readyReadStandardOutput.connect(self.__handleStdOutput)
        self.__process.readyReadStandardError.connect(self.__handleStdError)
        self.__process.stateChanged.connect(self.__handleStateChanged)
        self.__process.finished.connect(self.__handleProcessFinished)
        self.__process.started.connect(self.__handleProcessStarted)

    # endregion

    # region - Event Handlers
    def __handleProcessStarted(self):
        msg = f"[Action] Process Started {self.__server.name()}"
        signalBus.onLogToOutput.emit(msg)
        self.onLaunchSuccessful.emit(self.__server)

    def __handleProcessFinished(self, exitCode: int, exitStatus: QProcess.ExitStatus):
        msg = f"[Action] Process Finished {self.__server.name()}: {str(exitStatus)}, with exit code: {exitCode}"
        signalBus.onLogToOutput.emit(msg)

    def __handleStateChanged(self, state: QProcess.ProcessState):
        msg = f"[StateChanged] {self.__server.name()}: {str(state)}"
        signalBus.onLogToOutput.emit(msg)

    def __handleStdOutput(self):
        data = self.__process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        signalBus.onLogToOutput.emit(stdout)

    def __handleStdError(self):
        data = self.__process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        signalBus.onLogErrorToOutput.emit(stderr)

    def __handleErrorOccurred(self, error: QProcess.ProcessError):
        signalBus.onLogErrorToOutput.emit(f"Server process error: {error}")
        self.onLaunchFailed.emit(self.__server)

    # endregion

    # region - Workers
    def kill(self):

        # terminate the process
        self.__process.kill()

        # emit signal that the server has been killed
        self.onKill.emit(self.__server)

    def launch(self):
        self.__process.start(self.__command, self.__arguments[1:])

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters
    def command(self):
        return self.__command

    def server(self):
        return self.__server

    def arguments(self):
        return self.__arguments

    # endregion

    # region - Setters
    def setCommand(self, cmd: str):
        self.__command = cmd

    def setArguments(self, args: list[str]):
        self.__arguments = args

    def setServer(self, server: ServerModel):
        self.__server = server

    # endregion
