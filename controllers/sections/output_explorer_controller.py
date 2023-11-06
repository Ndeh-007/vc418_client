from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton

from views.components.section_header import SectionHeader
from views.sections.output_explorer import OutputExplorerView


class OutputExplorerController(OutputExplorerView):
    def __init__(self):
        super().__init__()
