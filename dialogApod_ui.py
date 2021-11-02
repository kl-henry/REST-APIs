# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogApod.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgApod(object):
    def setupUi(self, dlgApod):
        if not dlgApod.objectName():
            dlgApod.setObjectName(u"dlgApod")
        dlgApod.resize(487, 194)
        self.buttonBox = QDialogButtonBox(dlgApod)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(230, 130, 211, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgApod)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 436, 61))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbDatum = QLabel(self.layoutWidget)
        self.lbDatum.setObjectName(u"lbDatum")

        self.horizontalLayout.addWidget(self.lbDatum)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout.addWidget(self.dateEdit)

        self.pbLoadApod = QPushButton(dlgApod)
        self.pbLoadApod.setObjectName(u"pbLoadApod")
        self.pbLoadApod.setGeometry(QRect(10, 130, 88, 34))

        self.retranslateUi(dlgApod)
        self.buttonBox.accepted.connect(dlgApod.accept)
        self.buttonBox.rejected.connect(dlgApod.reject)

        QMetaObject.connectSlotsByName(dlgApod)
    # setupUi

    def retranslateUi(self, dlgApod):
        dlgApod.setWindowTitle(QCoreApplication.translate("dlgApod", u"Astronomy Picture of the Day (APOD)", None))
        self.lbDatum.setText(QCoreApplication.translate("dlgApod", u"Bitte Datum ausw\u00e4hlen:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("dlgApod", u"dd.MM.yyyy", None))
        self.pbLoadApod.setText(QCoreApplication.translate("dlgApod", u"hist. Bilder", None))
    # retranslateUi

