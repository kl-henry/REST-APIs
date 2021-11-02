# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogBored.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgBored(object):
    def setupUi(self, dlgBored):
        if not dlgBored.objectName():
            dlgBored.setObjectName(u"dlgBored")
        dlgBored.resize(591, 455)
        self.buttonBox = QDialogButtonBox(dlgBored)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(310, 350, 211, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.pbRandom = QPushButton(dlgBored)
        self.pbRandom.setObjectName(u"pbRandom")
        self.pbRandom.setGeometry(QRect(30, 100, 88, 34))
        self.gbBoredResult = QGroupBox(dlgBored)
        self.gbBoredResult.setObjectName(u"gbBoredResult")
        self.gbBoredResult.setGeometry(QRect(170, 100, 361, 221))
        self.gbBoredResult.setStyleSheet(u"QGroupBox { background-color: rgb(255, 255, 255);  border: 3px solid rgb(255, 0, 0); }")
        self.layoutWidget = QWidget(self.gbBoredResult)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 37, 79, 164))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbactivity = QLabel(self.layoutWidget)
        self.lbactivity.setObjectName(u"lbactivity")

        self.verticalLayout_2.addWidget(self.lbactivity)

        self.lbaccessibility = QLabel(self.layoutWidget)
        self.lbaccessibility.setObjectName(u"lbaccessibility")

        self.verticalLayout_2.addWidget(self.lbaccessibility)

        self.lbType_2 = QLabel(self.layoutWidget)
        self.lbType_2.setObjectName(u"lbType_2")

        self.verticalLayout_2.addWidget(self.lbType_2)

        self.lbParticipants = QLabel(self.layoutWidget)
        self.lbParticipants.setObjectName(u"lbParticipants")

        self.verticalLayout_2.addWidget(self.lbParticipants)

        self.lbPrice_2 = QLabel(self.layoutWidget)
        self.lbPrice_2.setObjectName(u"lbPrice_2")

        self.verticalLayout_2.addWidget(self.lbPrice_2)

        self.lbLink = QLabel(self.layoutWidget)
        self.lbLink.setObjectName(u"lbLink")

        self.verticalLayout_2.addWidget(self.lbLink)

        self.lbKey_2 = QLabel(self.layoutWidget)
        self.lbKey_2.setObjectName(u"lbKey_2")

        self.verticalLayout_2.addWidget(self.lbKey_2)

        self.layoutWidget1 = QWidget(self.gbBoredResult)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(110, 37, 241, 164))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbActivityDisplay = QLabel(self.layoutWidget1)
        self.lbActivityDisplay.setObjectName(u"lbActivityDisplay")

        self.verticalLayout_3.addWidget(self.lbActivityDisplay)

        self.lbAccessibilityDisplay = QLabel(self.layoutWidget1)
        self.lbAccessibilityDisplay.setObjectName(u"lbAccessibilityDisplay")

        self.verticalLayout_3.addWidget(self.lbAccessibilityDisplay)

        self.lbTypeDisplay = QLabel(self.layoutWidget1)
        self.lbTypeDisplay.setObjectName(u"lbTypeDisplay")

        self.verticalLayout_3.addWidget(self.lbTypeDisplay)

        self.lbParticipantsDisplay = QLabel(self.layoutWidget1)
        self.lbParticipantsDisplay.setObjectName(u"lbParticipantsDisplay")

        self.verticalLayout_3.addWidget(self.lbParticipantsDisplay)

        self.lbPriceDisplay = QLabel(self.layoutWidget1)
        self.lbPriceDisplay.setObjectName(u"lbPriceDisplay")

        self.verticalLayout_3.addWidget(self.lbPriceDisplay)

        self.lbLinkDisplay = QLabel(self.layoutWidget1)
        self.lbLinkDisplay.setObjectName(u"lbLinkDisplay")

        self.verticalLayout_3.addWidget(self.lbLinkDisplay)

        self.lbKeyDisplay = QLabel(self.layoutWidget1)
        self.lbKeyDisplay.setObjectName(u"lbKeyDisplay")

        self.verticalLayout_3.addWidget(self.lbKeyDisplay)


        self.retranslateUi(dlgBored)
        self.buttonBox.accepted.connect(dlgBored.accept)
        self.buttonBox.rejected.connect(dlgBored.reject)

        QMetaObject.connectSlotsByName(dlgBored)
    # setupUi

    def retranslateUi(self, dlgBored):
        dlgBored.setWindowTitle(QCoreApplication.translate("dlgBored", u"Dinge, die man tun kann", None))
        self.pbRandom.setText(QCoreApplication.translate("dlgBored", u"Vorschlag", None))
        self.gbBoredResult.setTitle(QCoreApplication.translate("dlgBored", u"Ergebnis", None))
        self.lbactivity.setText(QCoreApplication.translate("dlgBored", u"Activity:", None))
        self.lbaccessibility.setText(QCoreApplication.translate("dlgBored", u"Accessibility:", None))
        self.lbType_2.setText(QCoreApplication.translate("dlgBored", u"Typ:", None))
        self.lbParticipants.setText(QCoreApplication.translate("dlgBored", u"Participants:", None))
        self.lbPrice_2.setText(QCoreApplication.translate("dlgBored", u"Preis:", None))
        self.lbLink.setText(QCoreApplication.translate("dlgBored", u"Link:", None))
        self.lbKey_2.setText(QCoreApplication.translate("dlgBored", u"Schl\u00fcssel:", None))
        self.lbActivityDisplay.setText(QCoreApplication.translate("dlgBored", u"aaa", None))
        self.lbAccessibilityDisplay.setText(QCoreApplication.translate("dlgBored", u"bbb", None))
        self.lbTypeDisplay.setText(QCoreApplication.translate("dlgBored", u"ccc", None))
        self.lbParticipantsDisplay.setText(QCoreApplication.translate("dlgBored", u"ddd", None))
        self.lbPriceDisplay.setText(QCoreApplication.translate("dlgBored", u"eee", None))
        self.lbLinkDisplay.setText(QCoreApplication.translate("dlgBored", u"fff", None))
        self.lbKeyDisplay.setText(QCoreApplication.translate("dlgBored", u"ggg", None))
    # retranslateUi

