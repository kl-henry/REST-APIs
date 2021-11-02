# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogMarsRoverPicturesDisplay.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgMRPPicture(object):
    def setupUi(self, dlgMRPPicture):
        if not dlgMRPPicture.objectName():
            dlgMRPPicture.setObjectName(u"dlgMRPPicture")
        dlgMRPPicture.resize(676, 404)
        self.actionBildLaden = QAction(dlgMRPPicture)
        self.actionBildLaden.setObjectName(u"actionBildLaden")
        self.actionBildSpeichern = QAction(dlgMRPPicture)
        self.actionBildSpeichern.setObjectName(u"actionBildSpeichern")
        self.buttonBox = QDialogButtonBox(dlgMRPPicture)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(320, 360, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgMRPPicture)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 180, 123, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbMRPDate = QLabel(self.layoutWidget)
        self.lbMRPDate.setObjectName(u"lbMRPDate")

        self.verticalLayout.addWidget(self.lbMRPDate)

        self.lbMRPRover = QLabel(self.layoutWidget)
        self.lbMRPRover.setObjectName(u"lbMRPRover")

        self.verticalLayout.addWidget(self.lbMRPRover)

        self.lbMRPCamera = QLabel(self.layoutWidget)
        self.lbMRPCamera.setObjectName(u"lbMRPCamera")

        self.verticalLayout.addWidget(self.lbMRPCamera)

        self.lbMRPName = QLabel(self.layoutWidget)
        self.lbMRPName.setObjectName(u"lbMRPName")

        self.verticalLayout.addWidget(self.lbMRPName)

        self.lbLandLaunchDate = QLabel(self.layoutWidget)
        self.lbLandLaunchDate.setObjectName(u"lbLandLaunchDate")

        self.verticalLayout.addWidget(self.lbLandLaunchDate)

        self.layoutWidget1 = QWidget(dlgMRPPicture)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(150, 180, 511, 161))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbMRPDateDisplay = QLabel(self.layoutWidget1)
        self.lbMRPDateDisplay.setObjectName(u"lbMRPDateDisplay")

        self.verticalLayout_2.addWidget(self.lbMRPDateDisplay)

        self.lbMRPRoverDisplay = QLabel(self.layoutWidget1)
        self.lbMRPRoverDisplay.setObjectName(u"lbMRPRoverDisplay")

        self.verticalLayout_2.addWidget(self.lbMRPRoverDisplay)

        self.lbMRPCameraDisplay = QLabel(self.layoutWidget1)
        self.lbMRPCameraDisplay.setObjectName(u"lbMRPCameraDisplay")

        self.verticalLayout_2.addWidget(self.lbMRPCameraDisplay)

        self.lbMRPNameDisplay = QLabel(self.layoutWidget1)
        self.lbMRPNameDisplay.setObjectName(u"lbMRPNameDisplay")

        self.verticalLayout_2.addWidget(self.lbMRPNameDisplay)

        self.lbMRPLandLaunchDisplay = QLabel(self.layoutWidget1)
        self.lbMRPLandLaunchDisplay.setObjectName(u"lbMRPLandLaunchDisplay")

        self.verticalLayout_2.addWidget(self.lbMRPLandLaunchDisplay)

        self.layoutWidget2 = QWidget(dlgMRPPicture)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 110, 176, 36))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pbMRPPrevious = QPushButton(self.layoutWidget2)
        self.pbMRPPrevious.setObjectName(u"pbMRPPrevious")

        self.horizontalLayout.addWidget(self.pbMRPPrevious)

        self.pbMRPNext = QPushButton(self.layoutWidget2)
        self.pbMRPNext.setObjectName(u"pbMRPNext")

        self.horizontalLayout.addWidget(self.pbMRPNext)

        self.layoutWidget3 = QWidget(dlgMRPPicture)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 40, 651, 48))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbMRPPicture = QLabel(self.layoutWidget3)
        self.lbMRPPicture.setObjectName(u"lbMRPPicture")

        self.verticalLayout_3.addWidget(self.lbMRPPicture)

        self.lbMRPPictureLink = QLabel(self.layoutWidget3)
        self.lbMRPPictureLink.setObjectName(u"lbMRPPictureLink")
        self.lbMRPPictureLink.setFrameShape(QFrame.Box)
        self.lbMRPPictureLink.setFrameShadow(QFrame.Sunken)
        self.lbMRPPictureLink.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.lbMRPPictureLink)


        self.retranslateUi(dlgMRPPicture)
        self.buttonBox.accepted.connect(dlgMRPPicture.accept)
        self.buttonBox.rejected.connect(dlgMRPPicture.reject)

        QMetaObject.connectSlotsByName(dlgMRPPicture)
    # setupUi

    def retranslateUi(self, dlgMRPPicture):
        dlgMRPPicture.setWindowTitle(QCoreApplication.translate("dlgMRPPicture", u"Mars Rover Bilder", None))
        self.actionBildLaden.setText(QCoreApplication.translate("dlgMRPPicture", u"BildLaden", None))
#if QT_CONFIG(tooltip)
        self.actionBildLaden.setToolTip(QCoreApplication.translate("dlgMRPPicture", u"L\u00e4dt ausgew\u00e4hltes Bild", None))
#endif // QT_CONFIG(tooltip)
        self.actionBildSpeichern.setText(QCoreApplication.translate("dlgMRPPicture", u"BildSpeichern", None))
#if QT_CONFIG(tooltip)
        self.actionBildSpeichern.setToolTip(QCoreApplication.translate("dlgMRPPicture", u"Speichert aktuelles Bild", None))
#endif // QT_CONFIG(tooltip)
        self.lbMRPDate.setText(QCoreApplication.translate("dlgMRPPicture", u"Erddatum/Sol:", None))
        self.lbMRPRover.setText(QCoreApplication.translate("dlgMRPPicture", u"Rover:", None))
        self.lbMRPCamera.setText(QCoreApplication.translate("dlgMRPPicture", u"Kamera:", None))
        self.lbMRPName.setText(QCoreApplication.translate("dlgMRPPicture", u"Bildname:", None))
        self.lbLandLaunchDate.setText(QCoreApplication.translate("dlgMRPPicture", u"Gestartet/Gelandet:", None))
        self.lbMRPDateDisplay.setText(QCoreApplication.translate("dlgMRPPicture", u"aaa", None))
        self.lbMRPRoverDisplay.setText(QCoreApplication.translate("dlgMRPPicture", u"bbb", None))
        self.lbMRPCameraDisplay.setText(QCoreApplication.translate("dlgMRPPicture", u"ccc", None))
        self.lbMRPNameDisplay.setText(QCoreApplication.translate("dlgMRPPicture", u"ddd", None))
        self.lbMRPLandLaunchDisplay.setText(QCoreApplication.translate("dlgMRPPicture", u"eee", None))
#if QT_CONFIG(tooltip)
        self.pbMRPPrevious.setToolTip(QCoreApplication.translate("dlgMRPPicture", u"Vorheriges Bild", None))
#endif // QT_CONFIG(tooltip)
        self.pbMRPPrevious.setText(QCoreApplication.translate("dlgMRPPicture", u"<-", None))
#if QT_CONFIG(tooltip)
        self.pbMRPNext.setToolTip(QCoreApplication.translate("dlgMRPPicture", u"N\u00e4chstes Bild", None))
#endif // QT_CONFIG(tooltip)
        self.pbMRPNext.setText(QCoreApplication.translate("dlgMRPPicture", u"->", None))
        self.lbMRPPicture.setText(QCoreApplication.translate("dlgMRPPicture", u"Die Bilder k\u00f6nnen nur im Browser angezeigt werden. Bitte den folgenden Link anklicken:", None))
        self.lbMRPPictureLink.setText(QCoreApplication.translate("dlgMRPPicture", u"Link", None))
    # retranslateUi

