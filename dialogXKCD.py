import webbrowser

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QFileDialog

from RestAPIs_utilities import getImageFile
from dialogXKCD_ui import Ui_dlgXKCDoftheDay


class dlgWinXKCD(QDialog, Ui_dlgXKCDoftheDay):
    def __init__(self, response):
        super(dlgWinXKCD, self).__init__()
        self.setupUi(self)
        self.response = response

        self.fname = getImageFile(self.response["img"], "XKCD")
        # print(fname)
        pixmap = QPixmap(self.fname)
        self.lbXKCDComic.setPixmap(pixmap)
        self.lbXKCDComic.resize(pixmap.width(), pixmap.height())
        self.teXKCDAlt.insertPlainText(self.response["alt"])
        self.show()

        self.pbSave.clicked.connect(self.save_comic)
        self.pbBrowser.clicked.connect(self.show_in_browser)

    def show_in_browser(self):
        # print("dlgWinXKCD, show_in_browser: Enter", self.fname)
        webbrowser.get("firefox").open(self.fname)

    def save_comic(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);Image Files (*.png)", options=options)
        if fileName:
            # print(fileName)
            self.lbXKCDComic.pixmap().save(fileName)

