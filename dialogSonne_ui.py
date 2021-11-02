# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogSonne.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgSonne(object):
    def setupUi(self, dlgSonne):
        if not dlgSonne.objectName():
            dlgSonne.setObjectName(u"dlgSonne")
        dlgSonne.resize(324, 222)
        self.buttonBox = QDialogButtonBox(dlgSonne)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 160, 211, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgSonne)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 30, 234, 102))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbStandort = QLabel(self.layoutWidget)
        self.lbStandort.setObjectName(u"lbStandort")

        self.horizontalLayout.addWidget(self.lbStandort)

        self.cbStandort = QComboBox(self.layoutWidget)
        self.cbStandort.addItem("")
        self.cbStandort.addItem("")
        self.cbStandort.addItem("")
        self.cbStandort.setObjectName(u"cbStandort")
        self.cbStandort.setEditable(True)

        self.horizontalLayout.addWidget(self.cbStandort)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbVon = QLabel(self.layoutWidget)
        self.lbVon.setObjectName(u"lbVon")

        self.verticalLayout.addWidget(self.lbVon)

        self.deVonDat = QDateEdit(self.layoutWidget)
        self.deVonDat.setObjectName(u"deVonDat")
        self.deVonDat.setEnabled(False)
        self.deVonDat.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.deVonDat)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.deBisDat = QDateEdit(self.layoutWidget)
        self.deBisDat.setObjectName(u"deBisDat")
        self.deBisDat.setEnabled(False)
        self.deBisDat.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.deBisDat)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(dlgSonne)
        self.buttonBox.accepted.connect(dlgSonne.accept)
        self.buttonBox.rejected.connect(dlgSonne.reject)

        QMetaObject.connectSlotsByName(dlgSonne)
    # setupUi

    def retranslateUi(self, dlgSonne):
        dlgSonne.setWindowTitle(QCoreApplication.translate("dlgSonne", u"Sonnenauf/untergang", None))
        self.lbStandort.setText(QCoreApplication.translate("dlgSonne", u"Standort:", None))
        self.cbStandort.setItemText(0, QCoreApplication.translate("dlgSonne", u"Winnweiler", None))
        self.cbStandort.setItemText(1, QCoreApplication.translate("dlgSonne", u"Enkenbach-Alsenborn", None))
        self.cbStandort.setItemText(2, QCoreApplication.translate("dlgSonne", u"Kaiserslautern", None))

        self.cbStandort.setCurrentText(QCoreApplication.translate("dlgSonne", u"Winnweiler", None))
        self.lbVon.setText(QCoreApplication.translate("dlgSonne", u"von (Datum):", None))
        self.deVonDat.setDisplayFormat(QCoreApplication.translate("dlgSonne", u"dd.MM.yyyy", None))
        self.label_2.setText(QCoreApplication.translate("dlgSonne", u"bis (Datum):", None))
        self.deBisDat.setDisplayFormat(QCoreApplication.translate("dlgSonne", u"dd.MM.yyyy", None))
    # retranslateUi

