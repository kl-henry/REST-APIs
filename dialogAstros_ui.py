# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogAstros.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgAstros(object):
    def setupUi(self, dlgAstros):
        if not dlgAstros.objectName():
            dlgAstros.setObjectName(u"dlgAstros")
        dlgAstros.resize(608, 630)
        self.lbHeader = QLabel(dlgAstros)
        self.lbHeader.setObjectName(u"lbHeader")
        self.lbHeader.setGeometry(QRect(20, 40, 191, 18))
        self.layoutWidget = QWidget(dlgAstros)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 520, 514, 38))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbSave = QPushButton(self.layoutWidget)
        self.pbSave.setObjectName(u"pbSave")

        self.horizontalLayout.addWidget(self.pbSave)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)

        self.tvAstroList = QTreeView(dlgAstros)
        self.tvAstroList.setObjectName(u"tvAstroList")
        self.tvAstroList.setGeometry(QRect(20, 80, 511, 391))
        self.tvAstroList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.retranslateUi(dlgAstros)
        self.buttonBox.accepted.connect(dlgAstros.accept)
        self.buttonBox.rejected.connect(dlgAstros.reject)

        QMetaObject.connectSlotsByName(dlgAstros)
    # setupUi

    def retranslateUi(self, dlgAstros):
        dlgAstros.setWindowTitle(QCoreApplication.translate("dlgAstros", u"ASTROS - Astronauts in Space", None))
        self.lbHeader.setText(QCoreApplication.translate("dlgAstros", u"Astronauten derzeit im All:", None))
        self.pbSave.setText(QCoreApplication.translate("dlgAstros", u"Daten speichern", None))
    # retranslateUi

