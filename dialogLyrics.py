from PySide2.QtWidgets import QDialog, QFileDialog

from RestAPIs_utilities import getImageFile, request_Lyrics
from dialogLyrics_ui import Ui_dlgLyrics


class dlgWinLyrics(QDialog, Ui_dlgLyrics):
    def __init__(self):
        super(dlgWinLyrics, self).__init__()
        self.setupUi(self)
        self.show()

        self.pbSuchen.clicked.connect(self.execute_Suchen)
        self.pbSpeichern.clicked.connect(self.execute_Speichern)

    def execute_Suchen(self):
        result, response = request_Lyrics(self.leSinger.text().strip(), self.leSong.text().strip())
        if result == 200:
            self.teSongText.setText(response["lyrics"])

    def execute_Speichern(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);Image Files (*.txt)", options=options)
        if fileName:
            # print(fileName)
            with open(fileName, 'w') as myFile:
                myFile.write(str(self.teSongText.toPlainText()))
