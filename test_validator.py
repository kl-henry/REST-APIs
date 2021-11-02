from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QWidget, QLineEdit, QApplication

import sys


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.le_input = QLineEdit(self)

        ipRange = "(255|[-+]?[0-9]{1,3})"  # Part of the regular expression
        # Regulare expression
        ipRegex = QRegExp(ipRange + "\\," + ipRange + "\\," + ipRange)
        input_validator = QRegExpValidator(ipRegex, self.le_input)

        self.le_input.setValidator(input_validator)


if __name__ == '__main__':
    a = QApplication(sys.argv)

    w = MyWidget()
    w.show()

    a.exec_()
