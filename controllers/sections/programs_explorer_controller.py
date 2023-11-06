from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton

from views.components.section_header import SectionHeader
from views.sections.programs_explorer import ProgramsExplorerView


class ProgramsExplorerController(ProgramsExplorerView):
    def __init__(self):
        super().__init__()
