from PySide6.QtGui import QImage

from models.explorer.program_item_model import ProgramItemModel
from models.explorer.programs_list_model import ProgramListModel
from views.sections.programs_explorer import ProgramsExplorerView


class ProgramsExplorerController(ProgramsExplorerView):
    def __init__(self):
        super().__init__()
        file = QImage(':resources/images/file.png')
        data = [
            ProgramItemModel("File 1", file),
            ProgramItemModel("File 2", file),
            ProgramItemModel("File 3", file),
            ProgramItemModel("File 4", file),
            ProgramItemModel("File 4", file),
        ]

        model = ProgramListModel(data)
        self.programsListView.setModel(model)
