from PySide6.QtWidgets import QFrame, QVBoxLayout, QTabWidget, QStackedLayout

from views.components.preview_explorer_placeholder import PreviewExplorerPlaceholder


class PreviewExplorerView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.explorerLayout = QStackedLayout()
        self.explorerLayout.setContentsMargins(0, 0, 0, 0)

        # region placeholder

        placeholder = PreviewExplorerPlaceholder()
        self.explorerLayout.addWidget(placeholder)

        # endregion

        # region body

        body = QFrame()
        bodyLayout = QVBoxLayout()
        bodyLayout.setContentsMargins(0, 0, 0, 0)

        self.previewTabs = QTabWidget()
        self.previewTabs.setTabPosition(QTabWidget.TabPosition.North)
        self.previewTabs.setMovable(True)
        self.previewTabs.setTabsClosable(True)

        bodyLayout.addWidget(self.previewTabs)

        body.setLayout(bodyLayout)
        self.explorerLayout.addWidget(body)
        # endregion

        self.setLayout(self.explorerLayout)

        self.setObjectName("PreviewExplorer")
        self.previewTabs.setObjectName("PreviewTabs")
