from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QIntValidator

from views.components.playback_widget import PlayBackView


class PlayBackWidgetController(PlayBackView, QObject):
    onJumpToFrame = Signal(int)

    def __init__(self):
        super().__init__()
        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        self.framesInput.setText("0")
        self.framesTotal.setText("0")

    # endregion

    # region - Configure
    def __configure(self):
        self.framesInput.setValidator(QIntValidator())

        self.framesInput.textEdited.connect(self.__handleTextEdited)

    # endregion

    # region - Event Handlers
    def __handleTextEdited(self, text: str):
        """
        fires only when the value is changed manually by the user
        :return:
        """
        self.onJumpToFrame.emit(int(text))

    # endregion

    # region - Workers

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        pass

    # endregion

    # region - Getters
    def framesTotalValue(self):
        return int(self.framesTotal.text())

    def frameValue(self):
        return int(self.framesInput.text())

    # endregion

    # region - Setters
    def setFramesTotalValue(self, value: int):
        self.framesTotal.setText(str(value))

    def setFrameValue(self, value: int):
        self.framesInput.setText(str(value))
    # endregion
