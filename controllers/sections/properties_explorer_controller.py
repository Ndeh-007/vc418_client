from PySide6.QtGui import QIntValidator

from interfaces.structs import MenuBarActionType
from models.explorer.program_item_model import ProgramItemModel
from models.explorer.program_properties_model import ProgramPropertiesModel
from models.signal_data_models import SystemRequestData, SystemRequest
from utils.signal_bus import signalBus
from views.sections.properties_explorer import PropertyExplorerView

import store.settings as ss


class PropertyExplorerController(PropertyExplorerView):
    def __init__(self):
        super().__init__()
        self.__program: ProgramItemModel | None = None

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # initially nothing has been selected
        # show the placeholder
        self.__showPlaceholder(True)

        #  update the contents of the various inputs
        if self.__program is None:
            return
        self.__initializeInputs(self.__program.properties())

    # endregion

    # region - configure
    def __configure(self):

        # attach input validators to the inputs
        intValidator = QIntValidator()
        self.nProcsInput.setValidator(intValidator)

        # attach event handlers to inputs
        self.nProcsInput.textChanged.connect(self.__handleNProcsInputChanged)

        self.minimizeBtn.clicked.connect(self.__handleMinimizeBtnClicked)

    # endregion

    # region - event handlers
    def __handleNProcsInputChanged(self):
        self.__program.properties().setNProcs(int(self.nProcsInput.text()))

    def __handlePropertiesChanged(self):
        signalBus.onUpdateProgram.emit(self.__program)

    def __handleShowProgramDetailsSignal(self, item: ProgramItemModel | None):
        # if we have no data to update, show the placeholder
        if item is None:
            self.__showPlaceholder(True)
            return

        # read the data from store with the provided data.id()
        data = ss.APP_SETTINGS.PROGRAMS.programs(item.id())

        if data is None:
            return

        # update the local value
        self.__program = data

        # update the label of the properties
        self.programTitleLabel.setText(data.text())

        # initialize the inputs in the properties section
        self.__initializeInputs(data.properties())

        # toggle the placeholder
        self.__showPlaceholder(False)

    @staticmethod
    def __handleMinimizeBtnClicked():
        d = SystemRequestData(MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER, MenuBarActionType.TOGGLE_PROPERTIES_EXPLORER)
        r = SystemRequest(d)
        signalBus.onSystemRequest.emit(r)

    # endregion

    # region workers

    def __showPlaceholder(self, state: bool):
        """
        hides or shows the placeholder
        if state == true -> show else hide
        :param state:
        :return:
        """
        if state:
            self.contentLayout.setCurrentIndex(1)
        else:
            self.contentLayout.setCurrentIndex(0)

    def __initializeInputs(self, data: ProgramPropertiesModel):
        self.nProcsInput.setText(str(data.nProcs()))

    # endregion

    # region - connect signals

    def __connectSignals(self):
        signalBus.onShowProgramProperties.connect(self.__handleShowProgramDetailsSignal)

    # endregion
