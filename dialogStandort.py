from PySide2.QtWidgets import QDialog

from dialogStandort_ui import Ui_dlgStandort


class dlgWinStandort(QDialog, Ui_dlgStandort):
    def __init__(self):
        super(dlgWinStandort, self).__init__()
        self.setupUi(self)

