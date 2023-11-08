from views.sections.preview_explorer import PreviewExplorerView


class PreviewExplorerController(PreviewExplorerView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.explorerLayout.setCurrentIndex(0)

        self.initialize()

    def initialize(self):
        pass
