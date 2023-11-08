from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton

from views.components.section_header import SectionHeader
from views.sections.properties_explorer import PropertyExplorerView


class PropertyExplorerController(PropertyExplorerView):
    def __init__(self):
        super().__init__()
