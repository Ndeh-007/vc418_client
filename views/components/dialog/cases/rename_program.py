from typing import Callable

import qtawesome
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit

from models.explorer.program_item_model import ProgramItemModel
from views.components.dialog.dialog import CustomDialog, DialogControls
from styles.color import AppColors


class CustomRenameProgramDialog:
    """
    Creates a dialog that provides the user with the option of renaming the project
    """

    def __init__(self, parent, item: ProgramItemModel, handleUserResponse: Callable[[ProgramItemModel | None], None], acceptText="Yes", cancelText="ok",
                 icon: QIcon = None):
        """

        :param parent: the parent widget
        :param item: the message to be displayed by the dialog
        :param handleUserResponse: action to be performed when one of the tab buttons is clicked
        :param acceptText: the text to be shown on the accept slot
        :param cancelText: the text to be shown on the cancel slot
        :param icon: the icon type displayed to the user
        """
        # define props
        self.old_item = item
        self.new_item = item

        self.new_title: str | None = None
        # define ui
        content = QWidget()
        layout = QVBoxLayout()

        self.userAction = handleUserResponse

        self.icon = icon

        if icon is None:
            self.icon = qtawesome.icon("msc.info", color=AppColors().primary_rbg)

        label_icon = QPushButton()
        label_icon.setFlat(True)
        label_icon.setIcon(self.icon)
        label_icon.setIconSize(QSize(32, 32))

        body = QWidget()
        body_layout = QGridLayout()

        body_layout.addWidget(label_icon, 0, 0, 2, 1)

        input_title = QLabel("Enter new program name")
        self.new_title_input = QLineEdit()

        body_layout.addWidget(input_title, 0, 1)
        body_layout.addWidget(self.new_title_input, 1, 1)

        body.setLayout(body_layout)
        layout.addWidget(body)

        layout.addStretch()
        content.setLayout(layout)

        self.initialize()

        dlg_opts = DialogControls()
        dlg_opts.acceptText = acceptText
        dlg_opts.cancelText = cancelText
        self.dlg = CustomDialog("Rename Program", self.accept, self.reject, content, size="small",
                                dialog_controls=dlg_opts, parent=parent)

        # execute dialog
        self.dlg.exec_()

    def initialize(self):
        self.new_title_input.setText(self.old_item.text())
        self.new_title_input.selectAll()

    def accept(self):
        """
        the action performed when dialog is accepted
        :return:
        """
        new_title = self.new_title_input.text()

        # check if the new and old are the same, do not update
        if new_title == self.old_item.text():
            return
        self.new_item.setText(new_title)
        self.userAction(self.new_item)
        return

    def reject(self):
        """
        the action performed when dialog is rejected
        :return:
        """
        self.userAction(None)
        return
