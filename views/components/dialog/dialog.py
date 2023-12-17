from typing import Callable, Literal, Any

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QDialogButtonBox, QFrame, QGridLayout, QPushButton, QLabel, QHBoxLayout
from qframelesswindow import FramelessDialog

from styles.color import AppColors
from utils.signal_bus import signalBus
from utils.styling import setPaletteColor, q_read_style
from views.components.dialog.dialog_options import DialogControls, dialogControls


class CustomDialog(FramelessDialog):
    """
    Creates a custom dialog.
    """

    def __init__(self, dialog_title: str, on_accept: Callable[..., Any] | None, on_reject: Callable[..., Any] | None, content: QWidget = None,
                 size: None | Literal['small', 'large', 'medium', 'h-large', 'hh-large'] = None, parent: QWidget = None, dialog_target: str = None,
                 dialog_controls: DialogControls = dialogControls):
        """
        Initializes the custom dialog.
        :param dialog_title: The title of the dialog.
        :param on_accept: a function that is called when the dialog is accepted.
        :param on_reject: a function that is called when the dialog is cancelled.
        :param content: the UI contents of the dialog.
        :param size: the size of the dialog - large, medium, h-large, hh-large. If empty the dialog will take the size
                     of its contents
        :param parent: the parent widget that calls the dialog.
        :param dialog_target: the dialog's target content to display.
        :param dialog_controls: the controls properties of the dialog. Like what buttons to be shown.
        """
        super(CustomDialog, self).__init__()
        # self.setTitleBar(StandardTitleBar(self))
        self.dialog_controls = dialog_controls
        self.dialog_target = dialog_target
        self.setWindowTitle(dialog_title)
        self.setWindowIcon(QIcon(":resources/images/logo.png"))

        if size is None:
            self.resize(300, 100)

        if size == "small":
            self.resize(300, 100)

        if size == "large":
            self.resize(600, 500)

        if size == "medium":
            self.resize(400, 300)

        if size == "h-large":
            self.resize(800, 500)

        if size == "hh-large":
            self.resize(1000, 800)

        self.on_accept = on_accept
        self.on_reject = on_reject

        self.buttonBox = CustomDialogButtonBox(self.dialog_controls)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QGridLayout()

        head = CustomDialogTitle(QIcon(":resources/images/logo"), dialog_title)
        # head = QLabel("")

        body = QFrame()
        footer = QWidget()

        body.setObjectName("customDialogBody")
        body.setStyleSheet("""
            QFrame#customDialogBody{
            border-color:""" + AppColors().light_shade_rbg + """;
            border-style: solid;
            border-width: 1px 0px 1px 0px;
            }
        """)

        body.setContentsMargins(0, 0, 0, 0)
        body_layout = QGridLayout()
        body_layout.setContentsMargins(0, 0, 0, 0)
        if content is not None:
            content.setParent(self)
            body_layout.addWidget(content)
        body.setLayout(body_layout)

        footer.setContentsMargins(0, 0, 0, 0)
        footer_layout = QGridLayout()
        # footer_layout.setContentsMargins(0, 0, 0, 0)
        footer_layout.addWidget(self.buttonBox)
        footer.setLayout(footer_layout)

        layout.addWidget(head)
        layout.addWidget(body)
        layout.addWidget(footer)
        layout.setRowStretch(0, 0)
        layout.setRowMinimumHeight(0, 26)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        setPaletteColor(self, AppColors().light)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(q_read_style("dialog"))
        if dialog_target is not None:
            self.emit_signals()

        self.titleBar.raise_()

    def accept(self) -> None:
        if self.on_accept is None:
            self.done(1)
            return
        self.on_accept()
        self.done(1)

    def reject(self) -> None:
        if self.on_reject is None:
            self.done(0)
            return
        self.on_reject()
        self.done(0)

    def emit_signals(self):
        """
        emit the required signals when actions are performed
        :return:
        """
        signalBus.onShowConfigurationTargetItem.emit(self.dialog_target)


class CustomDialogButtonBox(QDialogButtonBox):
    """
    The box that contains the dialog data
    """

    def __init__(self, controls: DialogControls):
        """
        the controls of the dialog box
        :param controls:
        """
        super(CustomDialogButtonBox, self).__init__()
        self.btn_flag = QDialogButtonBox.StandardButton.Ok

        self.controls = dialogControls
        if controls is not None:
            self.controls = controls

        self.set_dialog_flags()
        self.style_buttons()

    def set_dialog_flags(self):
        """
        set the buttons used by the dialog
        :return:
        """
        self.btn_flag = QDialogButtonBox.StandardButton.Ok
        self.setStandardButtons(self.btn_flag)

        if self.controls.hasCancel:
            self.btn_flag = self.btn_flag | QDialogButtonBox.StandardButton.Cancel

            self.setStandardButtons(self.btn_flag)

    def style_buttons(self):
        """
        Style the buttons
        :return:
        """
        self.styleOkButton()
        if self.controls.hasCancel:
            self.styleOkButton()
            self.styleCancelButton()

    def styleOkButton(self):
        """
        style the primary dialog button. The "accept" button
        :return:
        """
        accept_button = self.button(QDialogButtonBox.StandardButton.Ok)
        accept_button.setText(self.controls.acceptText)
        accept_button.setStyleSheet(f"""
            color: {AppColors().light_rbg};
            border-radius: 2px;
            background: {self.controls.acceptButtonColor};
            padding: 5px 10px 5px 10px; 
            font-weight: 600;
        """)

    def styleCancelButton(self):
        """
        Style the secondary dialog buttons. e,g the 'cancel' button
        :return:
        """
        cancelButton = self.button(QDialogButtonBox.StandardButton.Cancel)
        cancelButton.setText(self.controls.cancelText)
        cancelButton.setStyleSheet(f"""
            color: {AppColors().medium_rbg};
            border-radius: 2px;
            background: {self.controls.cancelButtonColor};
            border: 1px solid {AppColors().medium_rbg};
            padding: 5px 10px 5px 10px; 
            font-weight: 600;
        """)


class CustomDialogTitle(QWidget):
    """
    creates a dialog title
    """

    def __init__(self, _icon: QIcon, text):
        """
        Set up the dialog's title with the required icon and text
        :param _icon: the icon to be shown by the dialog's header.
        :param text: the text to be shown in that title
        """
        super(CustomDialogTitle, self).__init__()
        self.IconSize = QSize(18, 18)
        self.HorizontalSpacing = 0
        layout = QHBoxLayout()
        layout.setContentsMargins(3, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignBaseline)

        icon = QPushButton()
        icon.setIcon(_icon)
        icon.setIconSize(self.IconSize)
        icon.setStyleSheet("")
        icon.setFlat(True)
        # icon.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(icon)
        layout.addSpacing(self.HorizontalSpacing)
        label = QLabel(text)
        label.setStyleSheet("font-size: 12px")
        layout.addWidget(label)

        layout.addStretch()
        self.setContentsMargins(5, 0, 0, 0)
        self.setStyleSheet("margin-top:6px")
        self.setLayout(layout)
