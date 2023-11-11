import uuid
from typing import Callable

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QComboBox, QLineEdit

from interfaces.structs import ProgramType
from models.explorer.program_item_model import ProgramItemModel
from views.components.dialog.dialog import CustomDialog
from views.components.dialog.dialog_options import DialogControls


class CreateNewProgram:
    """
    Opens a dialog for creating a new geometry
    """

    def __init__(self, parent, handleUserResponse: Callable[[ProgramItemModel | None], None]):

        self.userAction = handleUserResponse

        content = QWidget()
        layout = QVBoxLayout()

        inputs = QWidget()
        inputs_layout = QGridLayout()
        inputs_layout.setContentsMargins(0, 0, 0, 0)

        inputs_layout.addWidget(QLabel("Name: "), 0, 0)
        self.programNameInput = QLineEdit()
        inputs_layout.addWidget(self.programNameInput, 0, 1)

        inputs_layout.addWidget(QLabel("Program Type: "), 1, 0)
        self.programTypeComboBox = QComboBox()
        inputs_layout.addWidget(self.programTypeComboBox, 1, 1)

        inputs.setLayout(inputs_layout)

        layout.addWidget(inputs)
        layout.addStretch()
        content.setLayout(layout)

        # initialize content properties
        self.initialize()
        self.configure()

        dlg_opts = DialogControls()
        dlg_opts.acceptText = "Create"
        dlg_opts.hasCancel = True
        self.dlg = CustomDialog("New Program", self.accept, self.reject, content, dialog_controls=dlg_opts,
                                parent=parent)
        self.dlg.exec_()

    def accept(self):
        """
        Action performed when the dialog has been accepted. Checks if the geometry has already been created, if so it
        will ask if the user wishes to override the data, except in the case for intermediate where it will create and
        append a new intermediate
        :return:
        """
        _id = str(uuid.uuid4())
        _title = self.programNameInput.text()
        if _title == "":
            _title = self.__getTypeName()
        _type = self.programTypeComboBox.currentData()

        item = ProgramItemModel(text=_title, itemID=_id, programType=_type)
        self.userAction(item)

    def reject(self):
        self.userAction(None)

    def configure(self):
        """
        listen to changes in the type
        :return:
        """
        self.programTypeComboBox.currentIndexChanged.connect(self.__handleSelectionChanged)

    def initialize(self):
        """
        Initialize content properties
        :return:
        """

        self.programTypeComboBox.addItem("Reduce - Erlang", ProgramType.REDUCE_ERLANG)
        self.programTypeComboBox.addItem("Scan - Erlang", ProgramType.SCAN_ERLANG)

        self.programNameInput.setPlaceholderText(self.__getTypeName())

    def __getTypeName(self):
        t = self.programTypeComboBox.currentData()

        if t == ProgramType.SCAN_ERLANG:
            return "Scan (Erlang)"

        if t == ProgramType.REDUCE_ERLANG:
            return "Reduce (Erlang)"

    def __handleSelectionChanged(self, _):
        self.programNameInput.setPlaceholderText(self.__getTypeName())

