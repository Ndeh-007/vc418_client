from controllers.components.dialog.settings_general_tab_controller import SettingsGeneralTabContentController
from views.components.dialog.cases.settings_explorer import SettingsExplorerView


class SettingsExplorerController(SettingsExplorerView):
    def __init__(self):
        super().__init__()

        #   here we define the controls for the main settings page.l
        #   we instantiate the values of the tab

        generalTabContent = SettingsGeneralTabContentController()
        self.settingsTabWidget.addTab(generalTabContent, "General")
