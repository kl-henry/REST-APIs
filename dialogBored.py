import requests
from PySide2.QtWidgets import QDialog

from RestAPIs_utilities import request_Bored, jprint
from dialogBored_ui import Ui_dlgBored


class dlgWinBored(QDialog, Ui_dlgBored):
    def __init__(self):
        super(dlgWinBored, self).__init__()
        self.setupUi(self)

        self.pbRandom.clicked.connect(self.get_random_activity)

    def get_random_activity(self):
        # print("dlgWinBored get_random_activity: Enter")
        status, response = request_Bored()
        if status == 200:
            # print("get_random_activity success")
            # jprint(response)
            self.lbAccessibilityDisplay.setText(str(response["accessibility"]))
            self.lbActivityDisplay.setText(response["activity"])
            self.lbKeyDisplay.setText(str(response["key"]))
            self.lbLinkDisplay.setText(response["link"])
            self.lbParticipantsDisplay.setText(str(response["participants"]))
            self.lbPriceDisplay.setText(str(response["price"]))
            self.lbTypeDisplay.setText(response["type"])
