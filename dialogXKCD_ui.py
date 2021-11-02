# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogXKCD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgXKCDoftheDay(object):
    def setupUi(self, dlgXKCDoftheDay):
        if not dlgXKCDoftheDay.objectName():
            dlgXKCDoftheDay.setObjectName(u"dlgXKCDoftheDay")
        dlgXKCDoftheDay.resize(876, 698)
        self.lbAltText = QLabel(dlgXKCDoftheDay)
        self.lbAltText.setObjectName(u"lbAltText")
        self.lbAltText.setGeometry(QRect(20, 40, 131, 18))
        self.teXKCDAlt = QPlainTextEdit(dlgXKCDoftheDay)
        self.teXKCDAlt.setObjectName(u"teXKCDAlt")
        self.teXKCDAlt.setEnabled(True)
        self.teXKCDAlt.setGeometry(QRect(10, 80, 851, 87))
        self.teXKCDAlt.setReadOnly(True)
        self.lbXKCDComic = QLabel(dlgXKCDoftheDay)
        self.lbXKCDComic.setObjectName(u"lbXKCDComic")
        self.lbXKCDComic.setGeometry(QRect(20, 200, 681, 161))
        self.lbXKCDComic.setFrameShape(QFrame.Box)
        self.lbXKCDComic.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(dlgXKCDoftheDay)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(350, 630, 514, 38))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbBrowser = QPushButton(self.widget)
        self.pbBrowser.setObjectName(u"pbBrowser")

        self.horizontalLayout.addWidget(self.pbBrowser)

        self.pbSave = QPushButton(self.widget)
        self.pbSave.setObjectName(u"pbSave")

        self.horizontalLayout.addWidget(self.pbSave)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(dlgXKCDoftheDay)
        self.buttonBox.accepted.connect(dlgXKCDoftheDay.accept)
        self.buttonBox.rejected.connect(dlgXKCDoftheDay.reject)

        QMetaObject.connectSlotsByName(dlgXKCDoftheDay)
    # setupUi

    def retranslateUi(self, dlgXKCDoftheDay):
        dlgXKCDoftheDay.setWindowTitle(QCoreApplication.translate("dlgXKCDoftheDay", u"XKCD - Comic of the Day", None))
        self.lbAltText.setText(QCoreApplication.translate("dlgXKCDoftheDay", u"Alternativer Text:", None))
        self.lbXKCDComic.setText(QCoreApplication.translate("dlgXKCDoftheDay", u"TextLabel", None))
        self.pbBrowser.setText(QCoreApplication.translate("dlgXKCDoftheDay", u"Comic in Browser anzeigen", None))
        self.pbSave.setText(QCoreApplication.translate("dlgXKCDoftheDay", u"Comic speichern", None))
    # retranslateUi

