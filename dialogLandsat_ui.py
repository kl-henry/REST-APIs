# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogLandsat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgLandsat(object):
    def setupUi(self, dlgLandsat):
        if not dlgLandsat.objectName():
            dlgLandsat.setObjectName(u"dlgLandsat")
        dlgLandsat.resize(324, 325)
        self.buttonBox = QDialogButtonBox(dlgLandsat)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 250, 211, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.chInfo = QCheckBox(dlgLandsat)
        self.chInfo.setObjectName(u"chInfo")
        self.chInfo.setGeometry(QRect(10, 210, 61, 22))
        self.layoutWidget = QWidget(dlgLandsat)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 284, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbDatum = QLabel(self.layoutWidget)
        self.lbDatum.setObjectName(u"lbDatum")

        self.horizontalLayout.addWidget(self.lbDatum)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbLongitude = QLabel(self.layoutWidget)
        self.lbLongitude.setObjectName(u"lbLongitude")

        self.horizontalLayout_3.addWidget(self.lbLongitude)

        self.leLongitude = QLineEdit(self.layoutWidget)
        self.leLongitude.setObjectName(u"leLongitude")

        self.horizontalLayout_3.addWidget(self.leLongitude)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbLattitude = QLabel(self.layoutWidget)
        self.lbLattitude.setObjectName(u"lbLattitude")

        self.horizontalLayout_2.addWidget(self.lbLattitude)

        self.leLattitude = QLineEdit(self.layoutWidget)
        self.leLattitude.setObjectName(u"leLattitude")

        self.horizontalLayout_2.addWidget(self.leLattitude)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbDim = QLabel(self.layoutWidget)
        self.lbDim.setObjectName(u"lbDim")

        self.horizontalLayout_4.addWidget(self.lbDim)

        self.leDim = QLineEdit(self.layoutWidget)
        self.leDim.setObjectName(u"leDim")

        self.horizontalLayout_4.addWidget(self.leDim)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(dlgLandsat)
        self.buttonBox.accepted.connect(dlgLandsat.accept)
        self.buttonBox.rejected.connect(dlgLandsat.reject)

        QMetaObject.connectSlotsByName(dlgLandsat)
    # setupUi

    def retranslateUi(self, dlgLandsat):
        dlgLandsat.setWindowTitle(QCoreApplication.translate("dlgLandsat", u"Landsat Imagery", None))
        self.chInfo.setText(QCoreApplication.translate("dlgLandsat", u"Info", None))
        self.lbDatum.setText(QCoreApplication.translate("dlgLandsat", u"Bitte Datum ausw\u00e4hlen:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("dlgLandsat", u"dd.MM.yyyy", None))
        self.lbLongitude.setText(QCoreApplication.translate("dlgLandsat", u"geographische Breite:", None))
        self.lbLattitude.setText(QCoreApplication.translate("dlgLandsat", u"geographische L\u00e4nge:", None))
        self.lbDim.setText(QCoreApplication.translate("dlgLandsat", u"Bildausschnitt (in Grad, default 0.15):", None))
    # retranslateUi

