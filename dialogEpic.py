import datetime
from pathlib import Path
from urllib.request import urlretrieve
from PySide2.QtWidgets import QDialog
import matplotlib.pyplot as plt

import RestAPIs_utilities
from RestAPIs_constants import IMAGE_BASE
from dialogEpic_ui import Ui_dlgEpic


class dlgWinEpic(QDialog, Ui_dlgEpic):
    def __init__(self):
        super(dlgWinEpic, self).__init__()
        # print("dlgWinEpic Enter")
        self.setupUi(self)
        self.selected_date = ""
        self.epic_pictures = []
        self.dateEdit.setDate(datetime.date.today())

        self.pbGetEpic.clicked.connect(self.get_epic_picture)

    def get_epic_picture(self):
        # print("dlgWinEpic get_epic_picture Enter")
        nasa = RestAPIs_utilities.create_nasa_instance()
        d = self.dateEdit.date().toString("yyyy-MM-dd")
        col = self.cbNaturalEnhanced.currentText()
        # print("dlgWinEpic get_epic_picture Date, color", d, col)
        response = nasa.epic(color=col, date=d, available=True)
        # RestAPIs_utilities.jprint(response[0])
        # RestAPIs_utilities.jprint_to_file("test_data/epic_1_element"+date+".json", response[0])
        # print("dlgWinEpic get_epic_picture len(response)= ", len(response))
        if len(response) == 0:
            RestAPIs_utilities.show_info(self, winTitle="Hinweis", winInfo="Keine Bilder vorhanden")
        else:
            saved = 0
            year = d.split("-")[0]
            month = d.split("-")[1]
            day = d.split("-")[2]

            # print("dlgWinEpic get_epic_picture year, month, day= ", year, month, day)
            self.lbConstCount.setText(str(len(response)))
            completed = 0.0
            completed_ratio = 100 / len(response)
            self.progressBar.setValue(completed)
            for i in range(len(response)):
                # print("dlgWinEpic get_epic_picture Picture IDs:", response[i]["image"])
                IMAGE_ID = response[i]["image"]
                URL_EPIC = "https://epic.gsfc.nasa.gov/archive/" + self.cbNaturalEnhanced.currentText() + "/"
                URL_EPIC = URL_EPIC + year + '/' + month + '/' + day
                URL_EPIC = URL_EPIC + '/png'
                fileName = "test_data/" + IMAGE_ID + '.png'
                URL_EPIC = URL_EPIC + '/' + IMAGE_ID + '.png'
                # print("dlgWinEpic get_epic_picture Picture IDs:", URL_EPIC)
                self.lbFileIDName.setText(IMAGE_ID)
                try:
                    urlretrieve(URL_EPIC, fileName)
                    saved += 1
                    self.epic_pictures.append(fileName)
                    self.lbActualCount.setText(str(saved))
                    completed = completed + completed_ratio
                    self.progressBar.setValue(completed)
                except Exception as e:
                    print("Exception: " + str(e))
                    RestAPIs_utilities.show_info(self, winTitle="Fehler", winInfo=str(e))
            if saved > 0:
                RestAPIs_utilities.show_info(self, winTitle="Hinweis", winInfo="{0:d} Bilder gespeichert".format(saved))
                self.show_images(saved)

    def show_images(self, noof_images):
        columns = 5
        rows = (noof_images // 5) + 1
        width = int(round(IMAGE_BASE / rows, 0))
        height = int(round(IMAGE_BASE / rows, 0))
        fig = plt.figure(figsize=(height, width))
        for i in range(0, len(self.epic_pictures)):
            # print("dlgWinEpic get_epic_picture Picture IDs:", self.epic_pictures[i], len(self.epic_pictures))
            img = plt.imread(self.epic_pictures[i])
            sp = fig.add_subplot(rows, columns, i + 1)
            sp.set_title(Path(self.epic_pictures[i]).stem)
            sp.xaxis.set_visible(False)
            sp.yaxis.set_visible(False)
            plt.imshow(img)
        plt.show()
