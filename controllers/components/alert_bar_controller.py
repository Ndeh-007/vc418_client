import qtawesome

from interfaces.structs import AlertType
from models.common.signal_data_models import SystemAlert
from styles.color import appColors
from utils.signal_bus import signalBus
from views.components.alert_bar import AlertBarView
from utils.styling import setPaletteColor


class AlertBarController(AlertBarView):
    def __init__(self, showBannerIcon: bool = False):
        super().__init__(showBannerIcon=showBannerIcon)

        self.initialize()
        self.configure()

        self.__connectSignals()

    def initialize(self):
        self.__toggleVisibility(False)

    def configure(self):
        self.closeButton.clicked.connect(self.__handleCloseButtonClicked)

    def __toggleVisibility(self, state: bool):
        if state:
            self.show()
        else:
            self.hide()

    def erect(self, message: str, mode: AlertType = AlertType.Error):
        self.label.setText(message)

        if mode == AlertType.Error:
            self.label.setStyleSheet(f"color: {appColors.light_rbg};")
            ic = qtawesome.icon("msc.close", color=appColors.light_rbg)
            self.closeButton.setIcon(ic)
            setPaletteColor(self, appColors.danger_rbg)
            ic = qtawesome.icon("msc.info", color=appColors.light_rbg)
            self.bannerIconWidget.setIcon(ic)

        if mode == AlertType.Warning:
            self.label.setStyleSheet(f"color: {appColors.dark_rbg};")
            ic = qtawesome.icon("msc.close", color=appColors.dark_rbg)
            self.closeButton.setIcon(ic)
            setPaletteColor(self, appColors.warning_rbg)
            ic = qtawesome.icon("msc.info", color=appColors.dark_rbg)
            self.bannerIconWidget.setIcon(ic)

        if mode == AlertType.Event:
            self.label.setStyleSheet(f"color: {appColors.light_rbg};")
            ic = qtawesome.icon("msc.close", color=appColors.light_rbg)
            self.closeButton.setIcon(ic)
            setPaletteColor(self, appColors.primary_rbg)
            ic = qtawesome.icon("msc.info", color=appColors.light_rbg)
            self.bannerIconWidget.setIcon(ic)

        if mode == AlertType.Success:
            self.label.setStyleSheet(f"color: {appColors.light_rbg};")
            ic = qtawesome.icon("msc.close", color=appColors.light_rbg)
            self.closeButton.setIcon(ic)
            setPaletteColor(self, appColors.success_rbg)
            ic = qtawesome.icon("msc.info", color=appColors.light_rbg)
            self.bannerIconWidget.setIcon(ic)

        self.__toggleVisibility(True)

    def unErect(self):
        self.__toggleVisibility(False)

    # region - event handlers
    def __handleCloseButtonClicked(self):
        self.__toggleVisibility(self.closeButton.isHidden())

    def __handleSystemAlert(self, options: SystemAlert):
        self.erect(options.message(), options.alertType())

    # endregion

    def __connectSignals(self):
        signalBus.onSystemAlert.connect(self.__handleSystemAlert)
