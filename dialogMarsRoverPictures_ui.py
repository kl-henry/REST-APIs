# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogMarsRoverPictures.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgMarsRoverPictures(object):
    def setupUi(self, dlgMarsRoverPictures):
        if not dlgMarsRoverPictures.objectName():
            dlgMarsRoverPictures.setObjectName(u"dlgMarsRoverPictures")
        dlgMarsRoverPictures.resize(339, 425)
        icon = QIcon()
        icon.addFile(u"../../../Bilder/Icons/icons8-europa-96.png", QSize(), QIcon.Normal, QIcon.Off)
        dlgMarsRoverPictures.setWindowIcon(icon)
        self.layoutWidget = QWidget(dlgMarsRoverPictures)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(220, 370, 91, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)

        self.gbAuswahl = QGroupBox(dlgMarsRoverPictures)
        self.gbAuswahl.setObjectName(u"gbAuswahl")
        self.gbAuswahl.setGeometry(QRect(10, 10, 301, 301))
        self.pbGetMarsRoverPictures = QPushButton(self.gbAuswahl)
        self.pbGetMarsRoverPictures.setObjectName(u"pbGetMarsRoverPictures")
        self.pbGetMarsRoverPictures.setGeometry(QRect(150, 210, 111, 34))
        self.layoutWidget1 = QWidget(self.gbAuswahl)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 20, 241, 171))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gbDaten = QGroupBox(self.layoutWidget1)
        self.gbDaten.setObjectName(u"gbDaten")
        self.layoutWidget2 = QWidget(self.gbDaten)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 70, 201, 34))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.spMarsSol = QSpinBox(self.layoutWidget2)
        self.spMarsSol.setObjectName(u"spMarsSol")

        self.horizontalLayout_6.addWidget(self.spMarsSol)

        self.deEarthDate = QDateEdit(self.layoutWidget2)
        self.deEarthDate.setObjectName(u"deEarthDate")
        self.deEarthDate.setCalendarPopup(True)
        self.deEarthDate.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_6.addWidget(self.deEarthDate)

        self.layoutWidget3 = QWidget(self.gbDaten)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 120, 221, 34))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cbRover = QComboBox(self.layoutWidget3)
        self.cbRover.addItem("")
        self.cbRover.addItem("")
        self.cbRover.addItem("")
        self.cbRover.setObjectName(u"cbRover")

        self.horizontalLayout_3.addWidget(self.cbRover)

        self.cbCamera = QComboBox(self.layoutWidget3)
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.addItem("")
        self.cbCamera.setObjectName(u"cbCamera")

        self.horizontalLayout_3.addWidget(self.cbCamera)

        self.layoutWidget4 = QWidget(self.gbDaten)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 40, 202, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rbSol = QRadioButton(self.layoutWidget4)
        self.rbSol.setObjectName(u"rbSol")
        self.rbSol.setChecked(True)

        self.horizontalLayout_4.addWidget(self.rbSol)

        self.rbErdDatum = QRadioButton(self.layoutWidget4)
        self.rbErdDatum.setObjectName(u"rbErdDatum")

        self.horizontalLayout_4.addWidget(self.rbErdDatum)


        self.horizontalLayout.addWidget(self.gbDaten)

        self.layoutWidget5 = QWidget(dlgMarsRoverPictures)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 320, 301, 36))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbStatus = QLabel(self.layoutWidget5)
        self.lbStatus.setObjectName(u"lbStatus")

        self.horizontalLayout_5.addWidget(self.lbStatus)

        self.lbStatusDisplay = QLabel(self.layoutWidget5)
        self.lbStatusDisplay.setObjectName(u"lbStatusDisplay")
        self.lbStatusDisplay.setFrameShape(QFrame.Box)
        self.lbStatusDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.lbStatusDisplay)

        self.lbStatusText = QLabel(self.layoutWidget5)
        self.lbStatusText.setObjectName(u"lbStatusText")

        self.horizontalLayout_5.addWidget(self.lbStatusText)

        self.pbBilderAnzeigen = QPushButton(self.layoutWidget5)
        self.pbBilderAnzeigen.setObjectName(u"pbBilderAnzeigen")

        self.horizontalLayout_5.addWidget(self.pbBilderAnzeigen)


        self.retranslateUi(dlgMarsRoverPictures)
        self.buttonBox.accepted.connect(dlgMarsRoverPictures.accept)
        self.buttonBox.rejected.connect(dlgMarsRoverPictures.reject)

        self.pbGetMarsRoverPictures.setDefault(True)


        QMetaObject.connectSlotsByName(dlgMarsRoverPictures)
    # setupUi

    def retranslateUi(self, dlgMarsRoverPictures):
        dlgMarsRoverPictures.setWindowTitle(QCoreApplication.translate("dlgMarsRoverPictures", u"Mars Rover Pictures", None))
        self.gbAuswahl.setTitle(QCoreApplication.translate("dlgMarsRoverPictures", u"Bilddaten", None))
        self.pbGetMarsRoverPictures.setText(QCoreApplication.translate("dlgMarsRoverPictures", u"Ausf\u00fchren", None))
        self.gbDaten.setTitle(QCoreApplication.translate("dlgMarsRoverPictures", u"Auswahl", None))
        self.deEarthDate.setDisplayFormat(QCoreApplication.translate("dlgMarsRoverPictures", u"dd.MM.yyyy", None))
        self.cbRover.setItemText(0, QCoreApplication.translate("dlgMarsRoverPictures", u"curiosity", None))
        self.cbRover.setItemText(1, QCoreApplication.translate("dlgMarsRoverPictures", u"opportunity", None))
        self.cbRover.setItemText(2, QCoreApplication.translate("dlgMarsRoverPictures", u"spirit", None))

        self.cbCamera.setItemText(0, QCoreApplication.translate("dlgMarsRoverPictures", u"all", None))
        self.cbCamera.setItemText(1, QCoreApplication.translate("dlgMarsRoverPictures", u"FHAZ", None))
        self.cbCamera.setItemText(2, QCoreApplication.translate("dlgMarsRoverPictures", u"RHAZ", None))
        self.cbCamera.setItemText(3, QCoreApplication.translate("dlgMarsRoverPictures", u"MAST", None))
        self.cbCamera.setItemText(4, QCoreApplication.translate("dlgMarsRoverPictures", u"CHEMCAM", None))
        self.cbCamera.setItemText(5, QCoreApplication.translate("dlgMarsRoverPictures", u"MAHLI", None))
        self.cbCamera.setItemText(6, QCoreApplication.translate("dlgMarsRoverPictures", u"MARDI", None))
        self.cbCamera.setItemText(7, QCoreApplication.translate("dlgMarsRoverPictures", u"NAVCAM", None))
        self.cbCamera.setItemText(8, QCoreApplication.translate("dlgMarsRoverPictures", u"PANCAM", None))
        self.cbCamera.setItemText(9, QCoreApplication.translate("dlgMarsRoverPictures", u"MINITES", None))

        self.rbSol.setText(QCoreApplication.translate("dlgMarsRoverPictures", u"Sol", None))
        self.rbErdDatum.setText(QCoreApplication.translate("dlgMarsRoverPictures", u"Erddatum", None))
        self.lbStatus.setText(QCoreApplication.translate("dlgMarsRoverPictures", u"Bilder laden:", None))
        self.lbStatusDisplay.setText(QCoreApplication.translate("dlgMarsRoverPictures", u"0", None))
        self.lbStatusText.setText(QCoreApplication.translate("dlgMarsRoverPictures", u"geladen", None))
        self.pbBilderAnzeigen.setText(QCoreApplication.translate("dlgMarsRoverPictures", u"Bilder anzeigen", None))
    # retranslateUi

