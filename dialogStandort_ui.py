# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_Standort.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgStandort(object):
    def setupUi(self, dlgStandort):
        if not dlgStandort.objectName():
            dlgStandort.setObjectName(u"dlgStandort")
        dlgStandort.resize(313, 140)
        self.layoutWidget = QWidget(dlgStandort)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 234, 76))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbStandort = QLabel(self.layoutWidget)
        self.lbStandort.setObjectName(u"lbStandort")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbStandort.setFont(font)

        self.horizontalLayout.addWidget(self.lbStandort)

        self.cbStandort = QComboBox(self.layoutWidget)
        self.cbStandort.addItem("")
        self.cbStandort.addItem("")
        self.cbStandort.addItem("")
        self.cbStandort.setObjectName(u"cbStandort")
        self.cbStandort.setEditable(True)

        self.horizontalLayout.addWidget(self.cbStandort)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(dlgStandort)
        self.buttonBox.accepted.connect(dlgStandort.accept)
        self.buttonBox.rejected.connect(dlgStandort.reject)

        QMetaObject.connectSlotsByName(dlgStandort)
    # setupUi

    def retranslateUi(self, dlgStandort):
        dlgStandort.setWindowTitle(QCoreApplication.translate("dlgStandort", u"Auswahl Standort", None))
        self.lbStandort.setText(QCoreApplication.translate("dlgStandort", u"Standort:", None))
        self.cbStandort.setItemText(0, QCoreApplication.translate("dlgStandort", u"Winnweiler", None))
        self.cbStandort.setItemText(1, QCoreApplication.translate("dlgStandort", u"Kaiserslautern", None))
        self.cbStandort.setItemText(2, QCoreApplication.translate("dlgStandort", u"Enkenbach-Alsenborn", None))

    # retranslateUi

