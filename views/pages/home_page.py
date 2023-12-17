from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QSplitter, QGridLayout, QWidget

from controllers.components.alert_bar_controller import AlertBarController
from controllers.components.loading_bar_controller import LoadingBarController
from controllers.sections.output_explorer_controller import OutputExplorerController
from controllers.sections.preview_explorer_controller import PreviewExplorerController
from controllers.sections.programs_explorer_controller import ProgramsExplorerController
from controllers.sections.properties_explorer_controller import PropertyExplorerController


class HomePageView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.alertBar = AlertBarController(showBannerIcon=True)
        self.applicationBody = QWidget()
        applicationBodyLayout = QGridLayout()
        applicationBodyLayout.setContentsMargins(0, 0, 0, 0)
        applicationBodyLayout.setSpacing(0)
        self.loadingBar = LoadingBarController()

        self.programsExplorer = ProgramsExplorerController()
        self.outputExplorer = OutputExplorerController()
        self.propertiesExplorer = PropertyExplorerController()
        self.previewExplorer = PreviewExplorerController()

        self.topVerticalSplitter = QSplitter(Qt.Orientation.Horizontal)
        self.topVerticalSplitter.addWidget(self.programsExplorer)
        self.topVerticalSplitter.addWidget(self.previewExplorer)
        self.topVerticalSplitter.addWidget(self.propertiesExplorer)
        self.topVerticalSplitter.setSizes([250, 500, 200])

        self.horizontalSplitter = QSplitter(Qt.Orientation.Vertical)
        self.horizontalSplitter.addWidget(self.topVerticalSplitter)
        self.horizontalSplitter.addWidget(self.outputExplorer)
        self.horizontalSplitter.setSizes([500, 100])

        applicationBodyLayout.addWidget(self.horizontalSplitter)

        self.applicationBody.setLayout(applicationBodyLayout)

        layout.addWidget(self.alertBar)
        layout.addWidget(self.applicationBody)
        layout.addWidget(self.loadingBar)

        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 0)
        layout.setRowStretch(2, 0)

        self.setLayout(layout)
