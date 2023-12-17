from interfaces.structs import ServerType
from utils.helpers import selectFile, createSystemErrorAlert, selectDirectory
from views.components.dialog.settings_general_tab_content import SettingsGeneralTabContentView
import store.settings as ss
import os


class SettingsGeneralTabContentController(SettingsGeneralTabContentView):
    def __init__(self):
        super().__init__()

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # frame rate
        fps = ss.APP_SETTINGS.CONFIGURATION.animationFrequency()
        self.frameRateInput.setText(str(fps))

        # output file
        outputFle = ss.APP_SETTINGS.CONFIGURATION.httpResponseJSONFile()
        self.outputFile.setText(outputFle)

        # server path
        server = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        self.serverPathInput.setText(server.arguments()[0])

    # endregion

    # region - Configure
    def __configure(self):
        self.frameRateInput.textEdited.connect(self.__handleFrameRateChanged)
        self.outputFile.textChanged.connect(self.__handleFileChanged)
        self.outputFile.textChanged.connect(self.__handleServerPathChanged)
        self.selectOutputFileButton.clicked.connect(self.__handleOutputFileButtonClicked)
        self.selectServerPathButton.clicked.connect(self.__handleSelectServerPathButtonClicked)

    # endregion

    # region - Event Handlers
    def __handleServerPathChanged(self, _: str):
        path = self.serverPathInput.text()
        server = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        server.arguments()[0] = path
        ss.APP_SETTINGS.SERVER.updateServer(server.id(), server)

    def __handleSelectServerPathButtonClicked(self):
        path: str | None = selectDirectory()

        if path is None:
            return

        if not os.path.isdir(path):
            createSystemErrorAlert(f"Invalid Directory: '{path}' Does not Exist. Could not update server path")
            return

        if not os.path.isdir(path):
            createSystemErrorAlert(f"Invalid Directory: '{path}'. Could not update server path")
            return

        self.serverPathInput.setText(path)

    def __handleFileChanged(self, _: str):
        file: str = self.outputFile.text()
        ss.APP_SETTINGS.CONFIGURATION.setHttpResponseJSONFile(file)

    def __handleFrameRateChanged(self, _: str):
        text = self.frameRateInput.text()
        if text == "":
            return
        fps = int(text)
        ss.APP_SETTINGS.CONFIGURATION.setAnimationFrequency(fps)

    def __handleOutputFileButtonClicked(self):
        file: str | None = selectFile(self)

        if file is None:
            return
        if not os.path.isfile(file):
            createSystemErrorAlert(f"Invalid File. File '{file}' does not exist")
            return

        if not file.endswith(".json"):
            createSystemErrorAlert("Invalid File. File must be a '.json' file")
            return

        self.outputFile.setText(file)
    # endregion

    # region - Workers

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters

    # endregion

    # region - Setters

    # endregion

    # region - Override

    # endregion
