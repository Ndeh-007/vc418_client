from typing import Literal

import qtawesome
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtGui import QIntValidator

from interfaces.structs import AnimationPlayerState
from utils.signal_bus import signalBus
from views.components.playback_widget import PlayBackView

import store.settings as ss


class PlayBackWidgetController(PlayBackView, QObject):
    onJumpToFrame = Signal(int)
    onStartPlayback = Signal()
    onPausePlayback = Signal()
    onPlayerTimeout = Signal()

    def __init__(self):
        super().__init__()
        self.__playerState: AnimationPlayerState = AnimationPlayerState.OFF
        self.__timer = QTimer()

        self.__initialize()
        self.__configure()
        self.__connectSignals()

    # region - Initialize
    def __initialize(self):
        self.__initializeTimer()

        self.framesInput.setText("0")
        self.framesTotal.setText("0")

    # endregion

    # region - Configure
    def __configure(self):
        self.__timer.timeout.connect(self.__handleTimerTimeout)
        self.framesInput.setValidator(QIntValidator())
        self.framesInput.textEdited.connect(self.__handleTextEdited)

    # endregion

    # region - Event Handlers
    def __handleTimerTimeout(self):
        self.onPlayerTimeout.emit()

    def __handleTextEdited(self, text: str):
        """
        fires only when the value is changed manually by the user
        :return:
        """
        self.onJumpToFrame.emit(int(text))

    def __handleFrequencyChanged(self):
        """
        handles the changes in the frequency defined in the settings
        :return:
        """
        self.__initializeTimer()
        self.__timer.start()

    # endregion

    # region - Workers
    def __initializeTimer(self):
        fps = ss.APP_SETTINGS.CONFIGURATION.animationFrequency()
        time = int(1 / self.__computeFramesPerMilliseconds(fps))
        self.__timer.setInterval(time)

    def __computeFramesPerMilliseconds(self, value: int):
        """
        takes a value in frames per second and compute frames per millisecond
        :param value:
        :return:
        """
        return value / 1000

    def __changePlayIcon(self, target: Literal['play', 'pause']):
        if target == "play":
            ic = qtawesome.icon("fa5s.pause")
            self.playPauseBtn.setIcon(ic)
        if target == "pause":
            ic = qtawesome.icon("fa5s.play")
            self.playPauseBtn.setIcon(ic)

    def startPlayback(self):
        """
        resumes the player timer
        :return:
        """
        self.__timer.start()
        self.__playerState = AnimationPlayerState.ON
        self.__changePlayIcon('play')

    def stopPlayback(self):
        """
        stops the player timer
        :return:
        """
        self.__timer.stop()
        self.__playerState = AnimationPlayerState.OFF
        self.__changePlayIcon('pause')

    def isPaused(self):
        if self.__playerState == AnimationPlayerState.OFF:
            return True
        else:
            return False

    # endregion

    # region - Connect Signals

    def __connectSignals(self):
        signalBus.onSettingsFrameRateChanged.connect(self.__handleFrequencyChanged)

    # endregion

    # region - Getters
    def playerState(self):
        return self.__playerState

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
