from models.explorer.program_item_model import ProgramItemModel
from utils.signal_bus import signalBus


class ProgramManager:

    def __init__(self):
        super().__init__()

        self.__programs: dict[str, ProgramItemModel] = {}

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
    def __handleProgramUpdate(self, program: ProgramItemModel):
        self.__programs.update({program.id(): program})

    def __handleCreateProgram(self, program: ProgramItemModel):
        self.__programs.update({program.id(): program})

    def __handleDeleteProgram(self, program: ProgramItemModel):
        self.__programs.pop(program.id())

    # endregion

    # region - Workers

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        signalBus.onCreateProgram.connect(self.__handleCreateProgram)
        signalBus.onUpdateProgram.connect(self.__handleProgramUpdate)
        signalBus.onDeleteProgram.connect(self.__handleDeleteProgram)

    # endregion

    # region - Getters

    def programs(self, target: str = None):
        if target is not None:
            item = self.__programs.get(target)
            return item
        return self.__programs

    # endregion

    # region - Setters
    def setPrograms(self, data: dict[str, ProgramItemModel]):
        self.__programs = data

    # endregion
