# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogColors.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgColors(object):
    def setupUi(self, dlgColors):
        if not dlgColors.objectName():
            dlgColors.setObjectName(u"dlgColors")
        dlgColors.resize(1151, 273)
        self.buttonBox = QDialogButtonBox(dlgColors)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(1040, 220, 111, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.pbRequest = QPushButton(dlgColors)
        self.pbRequest.setObjectName(u"pbRequest")
        self.pbRequest.setGeometry(QRect(170, 220, 80, 30))
        self.gbColorDisplay = QGroupBox(dlgColors)
        self.gbColorDisplay.setObjectName(u"gbColorDisplay")
        self.gbColorDisplay.setGeometry(QRect(170, 20, 981, 181))
        self.layoutWidget = QWidget(self.gbColorDisplay)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 311, 44))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbColorBaseDescription = QLabel(self.layoutWidget)
        self.lbColorBaseDescription.setObjectName(u"lbColorBaseDescription")

        self.verticalLayout.addWidget(self.lbColorBaseDescription)

        self.lbColorBase = QLabel(self.layoutWidget)
        self.lbColorBase.setObjectName(u"lbColorBase")

        self.verticalLayout.addWidget(self.lbColorBase)

        self.layoutWidget_2 = QWidget(self.gbColorDisplay)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 110, 311, 44))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbColorBaseWithoutAlphaDescription = QLabel(self.layoutWidget_2)
        self.lbColorBaseWithoutAlphaDescription.setObjectName(u"lbColorBaseWithoutAlphaDescription")

        self.verticalLayout_2.addWidget(self.lbColorBaseWithoutAlphaDescription)

        self.lbColorBaseWithoutAlpha = QLabel(self.layoutWidget_2)
        self.lbColorBaseWithoutAlpha.setObjectName(u"lbColorBaseWithoutAlpha")

        self.verticalLayout_2.addWidget(self.lbColorBaseWithoutAlpha)

        self.layoutWidget_3 = QWidget(self.gbColorDisplay)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(340, 50, 311, 44))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbColorComplementaryDescription = QLabel(self.layoutWidget_3)
        self.lbColorComplementaryDescription.setObjectName(u"lbColorComplementaryDescription")

        self.verticalLayout_4.addWidget(self.lbColorComplementaryDescription)

        self.lbColorComplementary = QLabel(self.layoutWidget_3)
        self.lbColorComplementary.setObjectName(u"lbColorComplementary")

        self.verticalLayout_4.addWidget(self.lbColorComplementary)

        self.layoutWidget_4 = QWidget(self.gbColorDisplay)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(340, 110, 311, 44))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbComplementaryWithoutAlphaDescription = QLabel(self.layoutWidget_4)
        self.lbComplementaryWithoutAlphaDescription.setObjectName(u"lbComplementaryWithoutAlphaDescription")

        self.verticalLayout_5.addWidget(self.lbComplementaryWithoutAlphaDescription)

        self.lbComplementaryWithoutAlpha = QLabel(self.layoutWidget_4)
        self.lbComplementaryWithoutAlpha.setObjectName(u"lbComplementaryWithoutAlpha")

        self.verticalLayout_5.addWidget(self.lbComplementaryWithoutAlpha)

        self.layoutWidget_5 = QWidget(self.gbColorDisplay)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(660, 50, 311, 44))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbGrayScaleDescription = QLabel(self.layoutWidget_5)
        self.lbGrayScaleDescription.setObjectName(u"lbGrayScaleDescription")

        self.verticalLayout_6.addWidget(self.lbGrayScaleDescription)

        self.lbGrayScale = QLabel(self.layoutWidget_5)
        self.lbGrayScale.setObjectName(u"lbGrayScale")

        self.verticalLayout_6.addWidget(self.lbGrayScale)

        self.layoutWidget_6 = QWidget(self.gbColorDisplay)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(660, 110, 311, 44))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbGrayScaleWithoutAlphaDescription = QLabel(self.layoutWidget_6)
        self.lbGrayScaleWithoutAlphaDescription.setObjectName(u"lbGrayScaleWithoutAlphaDescription")

        self.verticalLayout_7.addWidget(self.lbGrayScaleWithoutAlphaDescription)

        self.lbGrayScaleWithoutAlpha = QLabel(self.layoutWidget_6)
        self.lbGrayScaleWithoutAlpha.setObjectName(u"lbGrayScaleWithoutAlpha")

        self.verticalLayout_7.addWidget(self.lbGrayScaleWithoutAlpha)

        self.layoutWidget1 = QWidget(dlgColors)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 137, 158))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbColorCode = QLabel(self.layoutWidget1)
        self.lbColorCode.setObjectName(u"lbColorCode")

        self.verticalLayout_3.addWidget(self.lbColorCode)

        self.leColorCode = QLineEdit(self.layoutWidget1)
        self.leColorCode.setObjectName(u"leColorCode")

        self.verticalLayout_3.addWidget(self.leColorCode)

        self.lbColorAlpha = QLabel(self.layoutWidget1)
        self.lbColorAlpha.setObjectName(u"lbColorAlpha")

        self.verticalLayout_3.addWidget(self.lbColorAlpha)

        self.sbAlpha = QSpinBox(self.layoutWidget1)
        self.sbAlpha.setObjectName(u"sbAlpha")
        self.sbAlpha.setMaximum(100)

        self.verticalLayout_3.addWidget(self.sbAlpha)

        self.cbColorFormat = QComboBox(self.layoutWidget1)
        self.cbColorFormat.addItem("")
        self.cbColorFormat.addItem("")
        self.cbColorFormat.addItem("")
        self.cbColorFormat.addItem("")
        self.cbColorFormat.addItem("")
        self.cbColorFormat.addItem("")
        self.cbColorFormat.setObjectName(u"cbColorFormat")

        self.verticalLayout_3.addWidget(self.cbColorFormat)


        self.retranslateUi(dlgColors)
        self.buttonBox.accepted.connect(dlgColors.accept)

        self.pbRequest.setDefault(True)


        QMetaObject.connectSlotsByName(dlgColors)
    # setupUi

    def retranslateUi(self, dlgColors):
        dlgColors.setWindowTitle(QCoreApplication.translate("dlgColors", u"Farb Konvertierung", None))
        self.pbRequest.setText(QCoreApplication.translate("dlgColors", u"Ausf\u00fchren", None))
        self.gbColorDisplay.setTitle(QCoreApplication.translate("dlgColors", u"Ergebnis", None))
        self.lbColorBaseDescription.setText(QCoreApplication.translate("dlgColors", u"Base:", None))
        self.lbColorBase.setText(QCoreApplication.translate("dlgColors", u"lbColorBase", None))
        self.lbColorBaseWithoutAlphaDescription.setText(QCoreApplication.translate("dlgColors", u"Base without Alpha:", None))
        self.lbColorBaseWithoutAlpha.setText(QCoreApplication.translate("dlgColors", u"lbBasewithoutAlpha", None))
        self.lbColorComplementaryDescription.setText(QCoreApplication.translate("dlgColors", u"Conplementary:", None))
        self.lbColorComplementary.setText(QCoreApplication.translate("dlgColors", u"lbColorBase", None))
        self.lbComplementaryWithoutAlphaDescription.setText(QCoreApplication.translate("dlgColors", u"Complementary without Alpha:", None))
        self.lbComplementaryWithoutAlpha.setText(QCoreApplication.translate("dlgColors", u"lbBasewithoutAlpha", None))
        self.lbGrayScaleDescription.setText(QCoreApplication.translate("dlgColors", u"GrayScale:", None))
        self.lbGrayScale.setText(QCoreApplication.translate("dlgColors", u"lbColorBase", None))
        self.lbGrayScaleWithoutAlphaDescription.setText(QCoreApplication.translate("dlgColors", u"GrayScale without Alpha:", None))
        self.lbGrayScaleWithoutAlpha.setText(QCoreApplication.translate("dlgColors", u"lbGrayScalewithoutAlpha", None))
        self.lbColorCode.setText(QCoreApplication.translate("dlgColors", u"Farb Code:", None))
        self.lbColorAlpha.setText(QCoreApplication.translate("dlgColors", u"Alpha:", None))
        self.cbColorFormat.setItemText(0, QCoreApplication.translate("dlgColors", u"Keyword", None))
        self.cbColorFormat.setItemText(1, QCoreApplication.translate("dlgColors", u"HEX", None))
        self.cbColorFormat.setItemText(2, QCoreApplication.translate("dlgColors", u"RGB", None))
        self.cbColorFormat.setItemText(3, QCoreApplication.translate("dlgColors", u"RGBA", None))
        self.cbColorFormat.setItemText(4, QCoreApplication.translate("dlgColors", u"HSL", None))
        self.cbColorFormat.setItemText(5, QCoreApplication.translate("dlgColors", u"HSLA", None))

    # retranslateUi

