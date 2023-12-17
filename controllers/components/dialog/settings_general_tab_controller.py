from views.components.dialog.settings_general_tab_content import SettingsGeneralTabContentView
import store.settings as ss


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

    # endregion

    # region - Configure
    def __configure(self):
        self.frameRateInput.textEdited.connect(self.__handleFrameRateChanged)
        self.outputFile.textEdited.connect(self.__handleFileChanged)
        self.selectOutputFileButton.clicked.connect(self.__handleOutputFileButtonClicked)

    # endregion

    # region - Event Handlers
    def __handleFileChanged(self, _: str):
        pass

    def __handleFrameRateChanged(self, _: str):
        pass

    def __handleOutputFileButtonClicked(self):
        pass

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
