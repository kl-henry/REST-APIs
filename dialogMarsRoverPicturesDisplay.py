import webbrowser
from pathlib import Path

from PySide2.QtWidgets import QDialog

import RestAPIs_utilities
from dialogMarsRoverPicturesDisplay_ui import Ui_dlgMRPPicture


class dlgWinMarsRoverPicturesDisplay(QDialog, Ui_dlgMRPPicture):
    def __init__(self, picture_list):
        super(dlgWinMarsRoverPicturesDisplay, self).__init__()
        print("dlgWinMarsRoverPicturesDisplay Enter")
        self.setupUi(self)
        self.picture_list = picture_list
        self.max_picture_count = len(self.picture_list)
        self.picture_count = 0

        self.lbMRPPictureLink.setOpenExternalLinks(True)

        self.pbMRPNext.clicked.connect(self.get_next_mars_rover_picture)
        self.pbMRPPrevious.clicked.connect(self.get_previous_mars_rover_picture)

        self.display_picture()

    def display_picture(self):
        # print("dlgWinMarsRoverPicturesDisplay display_picture Enter")
        picture = self.picture_list[self.picture_count]
        # RestAPIs_utilities.jprint(picture)
        self.lbMRPRoverDisplay.setText(picture["rover"]["name"])
        e_date = picture["earth_date"]
        earth_date = e_date.split("-")[2] + "." + e_date.split("-")[1] + "." + e_date.split("-")[0]
        self.lbMRPDateDisplay.setText(earth_date + " / " + str(picture["sol"]))
        self.lbMRPCameraDisplay.setText(picture["camera"]["name"] + ": " + picture["camera"]["full_name"])
        self.lbMRPPictureLink.setText(picture["img_src"])
        e_date = picture["rover"]["launch_date"]
        launching_date = e_date.split("-")[2] + "." + e_date.split("-")[1] + "." + e_date.split("-")[0]
        e_date = picture["rover"]["landing_date"]
        landing_date = e_date.split("-")[2] + "." + e_date.split("-")[1] + "." + e_date.split("-")[0]
        self.lbMRPLandLaunchDisplay.setText(launching_date + " / " + landing_date)
        # Display url using the default browser.If new is 0, the url is opened in the same browser
        # window if possible.If new is 1, a new browser window is opened if possible.
        # If new is 2, a new browser page(“tab”) is opened if possible.If autoraise is True, the window is raised
        # webbrowser.open(picture["img_src"], new=0, autoraise=True)
        # self.lbMRPPictureLink.setText("<a href=\"http://www.qtcentre.org\">QtCentre</a>")
        f_name = Path(picture["img_src"]).name
        self.lbMRPPictureLink.setText('<a href=\"' + picture["img_src"] + '"\>' + f_name + '</a>')

    def get_previous_mars_rover_picture(self):
        # print("dlgWinMarsRoverPicturesDisplay get_previous_mars_rover_picture Enter")
        if self.picture_count == 0:
            RestAPIs_utilities.show_info(self, winTitle="Hinweis", winInfo="Anfang der Liste erreicht")
        else:
            self.picture_count -= 1
        self.display_picture()

    def get_next_mars_rover_picture(self):
        # print("dlgWinMarsRoverPicturesDisplay get_next_mars_rover_picture Enter")
        if self.picture_count == self.max_picture_count:
            RestAPIs_utilities.show_info(self, winTitle="Hinweis", winInfo="Ende der Liste erreicht")
        else:
            self.picture_count += 1
        self.display_picture()
