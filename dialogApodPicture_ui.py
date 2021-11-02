# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogApodPicture.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgApodPicture(object):
    def setupUi(self, dlgApodPicture):
        if not dlgApodPicture.objectName():
            dlgApodPicture.setObjectName(u"dlgApodPicture")
        dlgApodPicture.resize(676, 650)
        self.actionBildLaden = QAction(dlgApodPicture)
        self.actionBildLaden.setObjectName(u"actionBildLaden")
        self.actionBildSpeichern = QAction(dlgApodPicture)
        self.actionBildSpeichern.setObjectName(u"actionBildSpeichern")
        self.buttonBox = QDialogButtonBox(dlgApodPicture)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(310, 590, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgApodPicture)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 310, 76, 116))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbApodDate = QLabel(self.layoutWidget)
        self.lbApodDate.setObjectName(u"lbApodDate")

        self.verticalLayout.addWidget(self.lbApodDate)

        self.lbApodMediaType = QLabel(self.layoutWidget)
        self.lbApodMediaType.setObjectName(u"lbApodMediaType")

        self.verticalLayout.addWidget(self.lbApodMediaType)

        self.lbApodHdurl = QLabel(self.layoutWidget)
        self.lbApodHdurl.setObjectName(u"lbApodHdurl")

        self.verticalLayout.addWidget(self.lbApodHdurl)

        self.lbApodCopyRight = QLabel(self.layoutWidget)
        self.lbApodCopyRight.setObjectName(u"lbApodCopyRight")

        self.verticalLayout.addWidget(self.lbApodCopyRight)

        self.layoutWidget1 = QWidget(dlgApodPicture)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(140, 310, 511, 116))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbApodDateDisplay = QLabel(self.layoutWidget1)
        self.lbApodDateDisplay.setObjectName(u"lbApodDateDisplay")

        self.verticalLayout_2.addWidget(self.lbApodDateDisplay)

        self.lbApodMediaTypeDisplay = QLabel(self.layoutWidget1)
        self.lbApodMediaTypeDisplay.setObjectName(u"lbApodMediaTypeDisplay")

        self.verticalLayout_2.addWidget(self.lbApodMediaTypeDisplay)

        self.lbApodHdurlDisplay = QLabel(self.layoutWidget1)
        self.lbApodHdurlDisplay.setObjectName(u"lbApodHdurlDisplay")

        self.verticalLayout_2.addWidget(self.lbApodHdurlDisplay)

        self.lbApodCopyRightDisplay = QLabel(self.layoutWidget1)
        self.lbApodCopyRightDisplay.setObjectName(u"lbApodCopyRightDisplay")

        self.verticalLayout_2.addWidget(self.lbApodCopyRightDisplay)

        self.lbApodExplanation = QLabel(dlgApodPicture)
        self.lbApodExplanation.setObjectName(u"lbApodExplanation")
        self.lbApodExplanation.setGeometry(QRect(60, 440, 74, 18))
        self.teApodExplanation = QPlainTextEdit(dlgApodPicture)
        self.teApodExplanation.setObjectName(u"teApodExplanation")
        self.teApodExplanation.setEnabled(True)
        self.teApodExplanation.setGeometry(QRect(140, 440, 511, 121))
        self.teApodExplanation.setReadOnly(True)
        self.lbApodPicture = QLabel(dlgApodPicture)
        self.lbApodPicture.setObjectName(u"lbApodPicture")
        self.lbApodPicture.setGeometry(QRect(60, 40, 571, 241))
        self.pbSpeichern = QPushButton(dlgApodPicture)
        self.pbSpeichern.setObjectName(u"pbSpeichern")
        self.pbSpeichern.setGeometry(QRect(40, 580, 88, 34))
        self.pbLaden = QPushButton(dlgApodPicture)
        self.pbLaden.setObjectName(u"pbLaden")
        self.pbLaden.setGeometry(QRect(140, 580, 88, 34))

        self.retranslateUi(dlgApodPicture)
        self.buttonBox.accepted.connect(dlgApodPicture.accept)
        self.buttonBox.rejected.connect(dlgApodPicture.reject)
        self.pbSpeichern.clicked.connect(self.actionBildSpeichern.trigger)
        self.pbLaden.clicked.connect(self.actionBildLaden.trigger)

        QMetaObject.connectSlotsByName(dlgApodPicture)
    # setupUi

    def retranslateUi(self, dlgApodPicture):
        dlgApodPicture.setWindowTitle(QCoreApplication.translate("dlgApodPicture", u"Apod Bild", None))
        self.actionBildLaden.setText(QCoreApplication.translate("dlgApodPicture", u"BildLaden", None))
#if QT_CONFIG(tooltip)
        self.actionBildLaden.setToolTip(QCoreApplication.translate("dlgApodPicture", u"L\u00e4dt ausgew\u00e4hltes Bild", None))
#endif // QT_CONFIG(tooltip)
        self.actionBildSpeichern.setText(QCoreApplication.translate("dlgApodPicture", u"BildSpeichern", None))
#if QT_CONFIG(tooltip)
        self.actionBildSpeichern.setToolTip(QCoreApplication.translate("dlgApodPicture", u"Speichert aktuelles Bild", None))
#endif // QT_CONFIG(tooltip)
        self.lbApodDate.setText(QCoreApplication.translate("dlgApodPicture", u"Datum:", None))
        self.lbApodMediaType.setText(QCoreApplication.translate("dlgApodPicture", u"Media Type:", None))
        self.lbApodHdurl.setText(QCoreApplication.translate("dlgApodPicture", u"Hdurl:", None))
        self.lbApodCopyRight.setText(QCoreApplication.translate("dlgApodPicture", u"Copyright:", None))
        self.lbApodDateDisplay.setText(QCoreApplication.translate("dlgApodPicture", u"aaa", None))
        self.lbApodMediaTypeDisplay.setText(QCoreApplication.translate("dlgApodPicture", u"bbb", None))
        self.lbApodHdurlDisplay.setText(QCoreApplication.translate("dlgApodPicture", u"ccc", None))
        self.lbApodCopyRightDisplay.setText(QCoreApplication.translate("dlgApodPicture", u"ddd", None))
        self.lbApodExplanation.setText(QCoreApplication.translate("dlgApodPicture", u"Erkl\u00e4rung:", None))
        self.lbApodPicture.setText(QCoreApplication.translate("dlgApodPicture", u"Apod Picture", None))
#if QT_CONFIG(tooltip)
        self.pbSpeichern.setToolTip(QCoreApplication.translate("dlgApodPicture", u"Speichert aktuelles Bild", None))
#endif // QT_CONFIG(tooltip)
        self.pbSpeichern.setText(QCoreApplication.translate("dlgApodPicture", u"Speichern", None))
#if QT_CONFIG(tooltip)
        self.pbLaden.setToolTip(QCoreApplication.translate("dlgApodPicture", u"L\u00e4dt ausgew\u00e4hltes Bild", None))
#endif // QT_CONFIG(tooltip)
        self.pbLaden.setText(QCoreApplication.translate("dlgApodPicture", u"Laden", None))
    # retranslateUi

