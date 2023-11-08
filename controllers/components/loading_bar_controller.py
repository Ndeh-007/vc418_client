from views.components.loading_bar import LoadingBarView


class LoadingBarController(LoadingBarView):
    def __init__(self):
        super().__init__()

        self.progressBar.hide()

        self.initialize()

    def initialize(self):
        pass
