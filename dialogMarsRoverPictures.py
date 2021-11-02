import datetime
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlretrieve
from PySide2.QtWidgets import QDialog
import matplotlib.pyplot as plt

import RestAPIs_utilities
from RestAPIs_constants import IMAGE_BASE
from dialogMarsRoverPicturesDisplay import dlgWinMarsRoverPicturesDisplay

from dialogMarsRoverPictures_ui import Ui_dlgMarsRoverPictures


class dlgWinMarsRoverPictures(QDialog, Ui_dlgMarsRoverPictures):
    def __init__(self):
        super(dlgWinMarsRoverPictures, self).__init__()
        # print("dlgWinMarsRoverPictures Enter")
        self.setupUi(self)
        self.selected_date = ""
        self.mars_pictures = []
        self.all_photos = []
        self.deEarthDate.setDate(datetime.date.today())

        self.pbGetMarsRoverPictures.clicked.connect(self.get_mars_rover_picture)
        self.pbBilderAnzeigen.clicked.connect(self.show_mars_rover_picture)

    def get_mars_rover_picture(self):
        print("dlgWinMarsRoverPictures get_mars_rover_picture Enter")
        nasa = RestAPIs_utilities.create_nasa_instance()
        if self.rbSol.isChecked():
            d = None
            sol = int(self.spMarsSol.value())
            dat = "sol" + str(sol)
        else:
            sol = None
            d = self.deEarthDate.date().toString("yyyy-MM-dd")
            dat = d
        rover = self.cbRover.currentText()
        camera = self.cbCamera.currentText()
        pic_count = 0
        page_no = 1
        response = nasa.mars_rover(sol=sol, earth_date=d, camera=camera, rover=rover, page=page_no)
        pic_count = pic_count + len(response)
        self.lbStatusDisplay.setText(str(pic_count))
        self.lbStatusDisplay.repaint()
        while len(response) > 0:
            for item in response:
                filename = "data/" + Path(item["img_src"]).stem + ".jpg"
                item["fname"] = filename
                self.all_photos.append(item)
            page_no += 1
            # print("dlgWinMarsRoverPictures get_epic_picture Params: EDate,Sol, rover, Camera, PageNo, pic_count",
            #       d, sol, rover, camera, page_no, len(response), pic_count)
            response = nasa.mars_rover(sol=sol, earth_date=d, camera=camera, rover=rover, page=page_no)
            pic_count = pic_count + len(response)
            self.lbStatusDisplay.setText(str(pic_count))
            self.lbStatusDisplay.repaint()
        # RestAPIs_utilities.jprint(self.all_photos)
        # RestAPIs_utilities.jprint_to_file("test_data/mars_rover"+rover+camera+dat+"_1.json", response[0])
        # print("dlgWinMarsRoverPictures get_mars_rover_picture len(response)= ", len(response))
        if len(response) == 0 and page_no == 1:
            RestAPIs_utilities.show_info(self, winTitle="Hinweis", winInfo="Keine Bildinfos vorhanden")
        else:
            RestAPIs_utilities.show_info(self, winTitle="Hinweis", winInfo="Alle Bildinfos geladen")

    def show_mars_rover_picture(self):
        print("dlgWinMarsRoverPictures show_mars_rover_picture Enter")
        dlgWin = dlgWinMarsRoverPicturesDisplay(self.all_photos)
        result = dlgWin.exec_()
