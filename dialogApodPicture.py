import datetime
import json
import os
import shutil
import urllib
from pathlib import Path

import nasapy
import requests
from PySide2.QtCore import Qt, QFileInfo
from PySide2.QtGui import QPixmap

from PySide2.QtWidgets import QDialog, QFileDialog

import RestAPIs_utilities
from RestAPIs_utilities import jprint
from dialogApodPicture_ui import Ui_dlgApodPicture


class dlgWinApodPicture(QDialog, Ui_dlgApodPicture):
    def __init__(self, selected_date=None):
        super(dlgWinApodPicture, self).__init__()
        self.setupUi(self)
        self.apod = ""
        self.filename_tmp = ""
        self.filename_save = ""
        if selected_date is None:
            self.load_apod()
        else:
            self.selected_date = selected_date.toString("yyyy-M-d")
            # print("dlgWinApodPicture __init__: selected_date= ", self.selected_date)
            styleString = "background-color: black; color: white"
            self.teApodExplanation.setStyleSheet(styleString)

            self.pbSpeichern.clicked.connect(self.save_apod)
            self.pbLaden.clicked.connect(self.load_apod)
            self.call_nasa()

    def call_nasa(self):
        nasa = RestAPIs_utilities.create_nasa_instance()
        d = self.selected_date
        # print("dlgWinApodPicture call_nasa: selected_date(d)= ", d)
        # Get the image data:
        self.apod = nasa.picture_of_the_day(date=d, hd=True)

        if (self.apod["media_type"] == "image"):

            # print("dlgWinApodPicture call_nasa: apod= ", apod)
            jprint(self.apod)
            # with open("test_data/test_apod"+d+".json", 'w') as outfile:
            #     json.dump(apod, outfile, sort_keys=True, indent=4)
            self.populate_apod_labels(self.apod)
            # Path of the directory:
            temp_dir = "/tmp"
            save_dir = "/home/heinz/Dokumente/Hintergrundbilder"
            title = d + "_" + self.apod["title"].replace(" ", "_").replace(":", "_") + ".jpg"
            self.filename_tmp = os.path.join(temp_dir, title)
            self.filename_save = os.path.join(save_dir, title)
            urllib.request.urlretrieve(url=self.apod["hdurl"], filename=self.filename_tmp)
            width = self.lbApodPicture.width()
            height = self.lbApodPicture.height()
            image = QPixmap(self.filename_tmp)
            self.lbApodPicture.setPixmap(image.scaled(width, height, Qt.KeepAspectRatio))
        else:
            print("Sorry, Image not available!")

    def populate_apod_labels(self, loc_apod=None):
        self.lbApodDateDisplay.setText(loc_apod["date"])
        self.lbApodHdurlDisplay.setText(loc_apod["hdurl"])
        try:
            self.lbApodCopyRightDisplay.setText(loc_apod["copyright"])
        except:
            self.lbApodCopyRightDisplay.setText("")
        self.lbApodMediaTypeDisplay.setText(loc_apod["media_type"])
        self.teApodExplanation.insertPlainText(loc_apod["explanation"])
        self.setWindowTitle(loc_apod["title"])

    def save_apod(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", self.filename_save,
                                                  "All Files (*);Image Files (*.jpg)",
                                                  options=options)
        if fileName:
            if '.jpg' not in fileName:
                fileName = fileName + ".jpg"
            # print("save_apod: ", fileName, self.filename_tmp)
            shutil.copy(self.filename_tmp, fileName)
            os.remove(self.filename_tmp)

            jsonFilename = fileName
            base = os.path.splitext(jsonFilename)[0]
            jsonFilename = base + ".json"
            # jprint(self.apod)

            with open(jsonFilename, 'w') as outfile:
                json.dump(self.apod, outfile, sort_keys=True, indent=4)

    def load_apod(self):
        # print("dlgWinApodPicture Enter")
        data = RestAPIs_utilities.load_apod(self)
        # print("load_apod: fname= ", data)
        if '.jpg' in data[0]:
            newfile = data[0].replace('.jpg', '.json')
        # print("dlgWinApodPicture: ", newfile)

        with open(newfile) as fd:
            json_data = json.load(fd)
        # jprint(json_data)
        self.populate_apod_labels(json_data)
        width = self.lbApodPicture.width()
        height = self.lbApodPicture.height()
        image = QPixmap(data[0])
        self.lbApodPicture.setPixmap(image.scaled(width, height, Qt.KeepAspectRatio))
