from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QSplitter, QPushButton, QGridLayout, QLabel, QWidget

from controllers.sections.output_explorer_controller import OutputExplorerController
from controllers.sections.programs_explorer_controller import ProgramsExplorerController
from controllers.sections.properties_explorer_controller import PropertiesExplorerController


class HomePageView(QFrame):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.alertBar = QPushButton("Alertbar")
        self.applicationBody = QWidget()
        applicationBodyLayout = QGridLayout()
        applicationBodyLayout.setSpacing(0)
        self.loadingBar = QPushButton("loading button")

        self.programsExplorer = ProgramsExplorerController()
        self.outputExplorer = OutputExplorerController()
        self.propertiesExplorer = PropertiesExplorerController()
        self.previewExplorer = QPushButton("btn")

        self.topVerticalSplitter = QSplitter(Qt.Orientation.Horizontal)
        self.topVerticalSplitter.addWidget(self.programsExplorer)
        self.topVerticalSplitter.addWidget(self.previewExplorer)
        self.topVerticalSplitter.addWidget(self.propertiesExplorer)
        self.topVerticalSplitter.setSizes([100, 600, 100])

        self.horizontalSplitter = QSplitter(Qt.Orientation.Vertical)
        self.horizontalSplitter.addWidget(self.topVerticalSplitter)
        self.horizontalSplitter.addWidget(self.outputExplorer)

        applicationBodyLayout.addWidget(self.horizontalSplitter)

        self.applicationBody.setLayout(applicationBodyLayout)

        layout.addWidget(self.alertBar)
        layout.addWidget(self.applicationBody)
        layout.addWidget(self.loadingBar)

        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 0)

        self.setLayout(layout)
