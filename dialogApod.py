import datetime

from PySide2.QtCore import SIGNAL
from PySide2.QtWidgets import QDialog

import RestAPIs_utilities
from dialogApod_ui import Ui_dlgApod
from dialogApodPicture import dlgWinApodPicture


class dlgWinApod(QDialog, Ui_dlgApod):
    def __init__(self):
        super(dlgWinApod, self).__init__()
        self.setupUi(self)
        self.dateEdit.setDate(datetime.date.today())
        self.connect(self.buttonBox, SIGNAL("accepted()"), self.my_accepted)
        self.pbLoadApod.clicked.connect(self.load_historic_picture)

    def my_accepted(self):
        # print("dlgWinApod: accepted Enter")
        # print("dlgWinApod: selected date: ", self.dateEdit.date())
        dlgWin = dlgWinApodPicture(self.dateEdit.date())
        result = dlgWin.exec_()

    def load_historic_picture(self):
        dlgWin = dlgWinApodPicture()
        result = dlgWin.exec_()

