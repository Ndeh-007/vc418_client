from PySide6.QtCore import QObject, Signal


class SignalBus(QObject):
    onServerStatusChanged = Signal(dict)


signalBus = SignalBus()
