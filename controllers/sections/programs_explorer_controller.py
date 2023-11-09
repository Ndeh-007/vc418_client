from PySide6.QtGui import QImage

from models.explorer.program_item_model import ProgramItemModel
from models.explorer.programs_list_model import ProgramListModel
from views.sections.programs_explorer import ProgramsExplorerView


class ProgramsExplorerController(ProgramsExplorerView):
    def __init__(self):
        super().__init__()
        self.model = ProgramListModel()
        self.programsListView.setModel(self.model)

        self.initialize()
        self.configure()

    # region - Initialize

    def initialize(self):
        file = QImage(':resources/images/file.png')
        data = [
            ProgramItemModel("File 1", file),
            ProgramItemModel("File 2", file),
            ProgramItemModel("File 3", file),
            ProgramItemModel("File 4", file),
            ProgramItemModel("File 4", file),
        ]
        self.model.addItems(data)
    # endregion

    # region - configure

    def configure(self):
        """
        connect required slots and signals
        :return:
        """
        self.model.onItemClicked.connect(self.handleListItemClicked)

    # end region

    # region - Event Handlers

    def handleListItemClicked(self, item: ProgramItemModel):
        pass

    # endregion
