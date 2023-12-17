from models.common.execution_step_model import ExecutionStepModel
from models.common.execution_timeline_model import ExecutionTimelineModel


class ProgramPropertiesModel:
    def __init__(self, nProcs: int = 4):
        self.__nProcs: int = nProcs
        self.__executionFrames: list[ExecutionStepModel] = []
        self.__executionTimelines: dict[str, ExecutionTimelineModel] = {}

    # region - Initialize

    def initialize(self, data):
        # sets the setting values for base program properties
        pass

    # endregion

    # region - Configure
    def __configure(self):
        pass

    # endregion

    # region - Event Handlers

    # endregion

    # region - Workers
    def clear(self):
        self.__executionFrames = []
        self.__executionTimelines = {}

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters
    def executionFrames(self):
        return self.__executionFrames

    def executionFrameAtIndex(self, index: int):
        if index not in range(0, len(self.__executionFrames)):
            return
        return self.__executionFrames[index]

    def executionTimeLine(self):
        return self.__executionTimelines

    def nProcs(self):
        return self.__nProcs

    # endregion

    # region - Setters
    def setExecutionFrames(self, data: list[ExecutionStepModel]):
        self.__executionFrames = data

    def updateExecutionTimeline(self, target: str, data: ExecutionTimelineModel):
        self.__executionTimelines.update({target: data})

    def setExecutionTimelines(self, data: ExecutionTimelineModel):
        self.__executionTimelines = data

    def setNProcs(self, value: int):
        self.__nProcs: int = value

    # endregion
