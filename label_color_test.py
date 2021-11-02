# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Label")

        # setting the geometry of window
        self.setGeometry(0, 0, 400, 300)

        # creating a label widget
        # by default label will display at top left corner
        self.label_1 = QLabel('Light green', self)

        # moving position
        self.label_1.move(100, 100)

        # setting up background color
        self.label_1.setStyleSheet("background-color: lightgreen")

        # creating a label widget
        # by default label will display at top left corner
        self.label_2 = QLabel('Yellow', self)

        # moving position
        self.label_2.move(100, 150)

        bgcolor = "yellow"
        # setting up background color and border
        self.label_2.setStyleSheet("background-color: " + "#7fffd4" + "; border: 1 px solid black;")

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())
