from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PySide6.QtGui import QIntValidator

from interfaces.structs import MenuBarActionType
from models.explorer.program_item_model import ProgramItemModel
from models.explorer.program_properties_model import ProgramPropertiesModel
from models.signal_data_models import SystemRequestData, SystemRequest
from utils.signal_bus import signalBus
from views.components.section_header import SectionHeader
from views.sections.properties_explorer import PropertyExplorerView


class PropertyExplorerController(PropertyExplorerView):
    def __init__(self):
        super().__init__()
        self.__propsData = ProgramPropertiesModel()

        self.__initialize()
        self.__configure()

        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        # initially nothing has been selected
        # show the placeholder
        self.__showPlaceholder(True)

        #  update the contents of the various inputs
        self.__initializeInputs(self.__propsData)

    # endregion

    # region - configure
    def __configure(self):

        # attach input validators to the inputs
        intValidator = QIntValidator()
        self.nProcsInput.setValidator(intValidator)

        self.minimizeBtn.clicked.connect(self.__handleMinimizeBtnClicked)

    # endregion

    # region - event handlers
    def __handleShowProgramDetailsSignal(self, data: ProgramItemModel | None):
        # if we have no data to update, show the placeholder
        print(data)
        if data is None:
            self.__showPlaceholder(True)
            return

        self.__propsData = data
        self.programTitleLabel.setText(data.text())
        self.__initializeInputs(data.properties())
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
