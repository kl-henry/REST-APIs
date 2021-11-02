# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# GET
# XKCD
# https://xkcd.com/info.0.json
# Returns the latest XKCD comic.
# # curl --location --request GET 'https://xkcd.com/info.0.json'

import sys
from PySide2.QtWidgets import QApplication

from mainRestAPIs import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
    # # result, response = request_xkcd()
    # result, response = request_astros()
    #
    # #
    # if result == 200:
    #     for people in response["people"]:
    #         print("Name: ", people["name"], "\t\tRaumschiff: ", people["craft"])
    #     jprint(response)
    # else:
    #     print("ASTROS Rest: Fehler beim Aufruf: ", result)
