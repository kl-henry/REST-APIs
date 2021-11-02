from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow

from RestAPIs_utilities import request_xkcd, request_Astros
from dialogApod import dlgWinApod
from dialogAstros import dlgWinAstros
from dialogBored import dlgWinBored
from dialogColors import dlgWinColors
from dialogEpic import dlgWinEpic
from dialogLyrics import dlgWinLyrics
from dialogMarsRoverPictures import dlgWinMarsRoverPictures
from dialogRecipeDB import dlgWinRecipeDB
from dialogWetter import dlgWinWetter
from dialogXKCD import dlgWinXKCD
from mainRestAPIs_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pbAstros.setIconSize(QSize(51, 51))
        self.pbLyrics.setIconSize(QSize(51, 51))
        self.pbXKCD.setIconSize(QSize(51, 51))
        self.pbBored.setIconSize(QSize(51, 51))
        self.pbColors.setIconSize(QSize(51, 51))
        self.pbWetter.setIconSize(QSize(51, 51))
        self.pbApod.setIconSize(QSize(51, 51))
        self.pbEpic.setIconSize(QSize(51, 51))
        self.pbMarsRoverPictures.setIconSize(QSize(51, 51))
        self.actionXkcd.triggered.connect(self.get_XKCD)
        self.actionAstros.triggered.connect(self.get_Astros)
        self.actionLyrics.triggered.connect(self.get_Lyrics)
        self.actionBored.triggered.connect(self.get_Bored)
        self.actionColors.triggered.connect(self.get_Colors)
        self.actionWetter.triggered.connect(self.get_Wetter)
        self.actionGetApod.triggered.connect(self.get_Apod)
        self.actionNasaEpic.triggered.connect(self.get_Epic)
        self.actionMarsRoverPictures.triggered.connect(self.get_mars_rover_pictures)
        self.actionRecipeDB.triggered.connect(self.get_RecipeDB)
        self.show()

    def get_XKCD(self):
        result, response = request_xkcd()
        # jprint(response)
        if result == 200:
            # print("xkcd, alt: ", response["alt"])
            # print("xkcd, img: ", response["img"])
            # webbrowser.get("firefox").open(response["img"])
            # fname = getImageFile(response["img"], "XKCD")
            # print(fname)
            dlgWin = dlgWinXKCD(response)

            result = dlgWin.exec_()

            # print("result: ", result)
        else:
            print("XKCD Rest: Fehler beim Aufruf: ", result)

    def get_Astros(self):
        # print("MainWindow: get_Astros")
        result, response = request_Astros()
        # jprint(response)
        if result == 200:
            # print("get_Astros: success")
            dlgWin = dlgWinAstros(response)
            result = dlgWin.exec_()

    def get_Lyrics(self):
        # print("MainWindow: get_Lyrics")

        dlgWin = dlgWinLyrics()
        result = dlgWin.exec_()

    def get_Bored(self):
        # print("MainWindow: get_Bored")

        dlgWin = dlgWinBored()
        result = dlgWin.exec_()

    def get_Colors(self):
        # print("MainWindow: get_Colors")

        dlgWin = dlgWinColors()
        result = dlgWin.exec_()

    def get_Wetter(self):
        # print("MainWindow: get_Wetter")
        dlgWin = dlgWinWetter()
        result = dlgWin.exec_()

    def get_Apod(self):
        # print("MainWindow: get_Apod")
        dlgWin = dlgWinApod()
        result = dlgWin.exec_()

    def get_Epic(self):
        # print("MainWindow: get_Epic")
        dlgWin = dlgWinEpic()
        result = dlgWin.exec_()

    def get_mars_rover_pictures(self):
        # print("MainWindow: get_mars_rover_pictures")
        dlgWin = dlgWinMarsRoverPictures()
        result = dlgWin.exec_()

    def get_RecipeDB(self):
        # print("MainWindow: get_MovieDB")
        dlgWin = dlgWinRecipeDB()
        result = dlgWin.exec_()
