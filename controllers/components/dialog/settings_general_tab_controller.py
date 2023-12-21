from interfaces.structs import ServerType
from utils.helpers import selectFile, createSystemErrorAlert, selectDirectory
from views.components.dialog.settings_general_tab_content import SettingsGeneralTabContentView
import store.settings as ss
import os
from PySide6.QtGui import QIntValidator


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

        # protocol
        self.protocolSelectionComboBox.addItem("http", "http")
        self.protocolSelectionComboBox.addItem("https", "https")

        # rebar location
        rebarLocation = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG).command()
        self.rebarLocation.setText(rebarLocation)

        # domain
        domain = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG).domain()
        self.domainInput.setText(domain)

        # port number
        port = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG).port()
        self.portNumberInput.setText(str(port))

    # endregion

    # region - Configure
    def __configure(self):
        self.portNumberInput.setValidator(QIntValidator())
        self.frameRateInput.setValidator(QIntValidator())

        self.frameRateInput.textEdited.connect(self.__handleFrameRateChanged)
        self.outputFile.textChanged.connect(self.__handleFileChanged)
        self.serverPathInput.textChanged.connect(self.__handleServerPathChanged)
        self.selectOutputFileButton.clicked.connect(self.__handleOutputFileButtonClicked)
        self.selectServerPathButton.clicked.connect(self.__handleSelectServerPathButtonClicked)

        self.rebarLocation.textChanged.connect(self.__handleRebarLocationTextChanged)
        self.selectRebarFileButton.clicked.connect(self.__handleSelectRebarFileClicked)

        self.protocolSelectionComboBox.currentIndexChanged.connect(self.__handleProtocolCurrentIndexChanged)
        self.portNumberInput.textEdited.connect(self.__handlePortNumberTextChanged)
        self.domainInput.textEdited.connect(self.__handleDomainInputTextChanged)

    # endregion

    # region - Event Handlers

    def __handleRebarLocationTextChanged(self, _: str):
        file = self.rebarLocation.text()
        if file == "":
            createSystemErrorAlert(f"Invalid file for rebar. {file}")
            return

        server = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        server.setCommand(file)
        ss.APP_SETTINGS.SERVER.updateServer(server.id(), server)

    def __handleSelectRebarFileClicked(self):
        file: str | None = selectFile(self)
        if file is None:
            return
        self.rebarLocation.setText(file)

    def __handleProtocolCurrentIndexChanged(self, index):
        protocol: str = self.protocolSelectionComboBox.itemData(index)
        server = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        server.setHTTPMode(protocol)
        ss.APP_SETTINGS.SERVER.updateServer(server.id(), server)

    def __handlePortNumberTextChanged(self, _: str):
        value = self.portNumberInput.text()
        if value == "":
            return
        server = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        server.setPort(int(value))
        ss.APP_SETTINGS.SERVER.updateServer(server.id(), server)

    def __handleDomainInputTextChanged(self, _: str):
        value = self.domainInput.text()
        if value == "":
            return
        server = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        server.setDomain(value)
        ss.APP_SETTINGS.SERVER.updateServer(server.id(), server)

    def __handleServerPathChanged(self, _: str):
        path = self.serverPathInput.text()
        server = ss.APP_SETTINGS.SERVER.servers(ServerType.ERLANG)
        args = server.arguments()
        args[0] = path
        server.setArguments(args)
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
        if int(text) == "0":
            text = 1
            self.frameRateInput.setText("1")
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
