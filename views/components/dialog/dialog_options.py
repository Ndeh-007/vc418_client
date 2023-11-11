from styles.color import appColors


class DialogControls:
    """
    Define the dialog options. What buttons the custom dialog should show and the appropriate text
    """
    def __init__(self):
        self.cancelButtonColor = appColors.light_shade_rbg
        self.acceptButtonColor = appColors.primary_rbg
        self.hasCancel = True
        self.cancelText = "Cancel"
        self.acceptText = "OK"
        self.hasApply = False
        self.applyText = "Apply"


dialogControls = DialogControls()

