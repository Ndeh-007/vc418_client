from controllers.components.dialog.settings_explorer_controller import SettingsExplorerController
from utils.signal_bus import signalBus
from views.components.dialog.dialog import CustomDialog
from views.components.dialog.dialog_options import DialogControls


class SettingsExplorerDialogController:
    def __init__(self):
        options = DialogControls()
        options.hasCancel = False
        content = SettingsExplorerController()
        self.__settingsDialog = CustomDialog("Settings", content=content, on_accept=None, on_reject=None,
                                             dialog_controls=options)

        self.connectSignals()

    def launchDialog(self):
        self.__settingsDialog.updateFrameless()
        self.__settingsDialog.exec()

    def connectSignals(self):
        signalBus.onOpenSettings.connect(self.launchDialog)
