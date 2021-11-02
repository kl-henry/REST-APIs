# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogRecipeDB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgRecipeDB(object):
    def setupUi(self, dlgRecipeDB):
        if not dlgRecipeDB.objectName():
            dlgRecipeDB.setObjectName(u"dlgRecipeDB")
        dlgRecipeDB.resize(785, 538)
        self.buttonBox = QDialogButtonBox(dlgRecipeDB)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(410, 490, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.pbSuchen = QPushButton(dlgRecipeDB)
        self.pbSuchen.setObjectName(u"pbSuchen")
        self.pbSuchen.setGeometry(QRect(370, 197, 88, 34))
        self.gbSuchen = QGroupBox(dlgRecipeDB)
        self.gbSuchen.setObjectName(u"gbSuchen")
        self.gbSuchen.setGeometry(QRect(30, 10, 331, 221))
        self.layoutWidget = QWidget(self.gbSuchen)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 308, 181))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbIngredient = QLabel(self.layoutWidget)
        self.lbIngredient.setObjectName(u"lbIngredient")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbIngredient)

        self.leIngredient = QLineEdit(self.layoutWidget)
        self.leIngredient.setObjectName(u"leIngredient")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leIngredient)

        self.lbCuisine = QLabel(self.layoutWidget)
        self.lbCuisine.setObjectName(u"lbCuisine")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbCuisine)

        self.cbCuisine = QComboBox(self.layoutWidget)
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.addItem("")
        self.cbCuisine.setObjectName(u"cbCuisine")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cbCuisine)

        self.lbType = QLabel(self.layoutWidget)
        self.lbType.setObjectName(u"lbType")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbType)

        self.cbType = QComboBox(self.layoutWidget)
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.setObjectName(u"cbType")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cbType)

        self.lbReadyTime = QLabel(self.layoutWidget)
        self.lbReadyTime.setObjectName(u"lbReadyTime")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbReadyTime)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spReadyTime = QSpinBox(self.layoutWidget)
        self.spReadyTime.setObjectName(u"spReadyTime")
        self.spReadyTime.setMaximum(120)

        self.horizontalLayout.addWidget(self.spReadyTime)

        self.lbMin = QLabel(self.layoutWidget)
        self.lbMin.setObjectName(u"lbMin")

        self.horizontalLayout.addWidget(self.lbMin)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.twRecipes = QTableWidget(dlgRecipeDB)
        if (self.twRecipes.columnCount() < 2):
            self.twRecipes.setColumnCount(2)
        self.twRecipes.setObjectName(u"twRecipes")
        self.twRecipes.setGeometry(QRect(30, 250, 721, 231))
        self.twRecipes.setColumnCount(2)
        self.layoutWidget1 = QWidget(dlgRecipeDB)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(370, 10, 381, 181))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbQueryString = QLabel(self.layoutWidget1)
        self.lbQueryString.setObjectName(u"lbQueryString")

        self.verticalLayout.addWidget(self.lbQueryString)

        self.teQueryString = QTextEdit(self.layoutWidget1)
        self.teQueryString.setObjectName(u"teQueryString")
        self.teQueryString.setFrameShape(QFrame.Box)
        self.teQueryString.setReadOnly(True)

        self.verticalLayout.addWidget(self.teQueryString)

        self.pbDetail = QPushButton(dlgRecipeDB)
        self.pbDetail.setObjectName(u"pbDetail")
        self.pbDetail.setGeometry(QRect(30, 490, 88, 34))
        QWidget.setTabOrder(self.cbCuisine, self.cbType)
        QWidget.setTabOrder(self.cbType, self.spReadyTime)

        self.retranslateUi(dlgRecipeDB)
        self.buttonBox.accepted.connect(dlgRecipeDB.accept)
        self.buttonBox.rejected.connect(dlgRecipeDB.reject)

        QMetaObject.connectSlotsByName(dlgRecipeDB)
    # setupUi

    def retranslateUi(self, dlgRecipeDB):
        dlgRecipeDB.setWindowTitle(QCoreApplication.translate("dlgRecipeDB", u"Rezepte Datenbank", None))
        self.pbSuchen.setText(QCoreApplication.translate("dlgRecipeDB", u"Suchen", None))
        self.gbSuchen.setTitle(QCoreApplication.translate("dlgRecipeDB", u"Suchen", None))
        self.lbIngredient.setText(QCoreApplication.translate("dlgRecipeDB", u"Zutat:", None))
        self.lbCuisine.setText(QCoreApplication.translate("dlgRecipeDB", u"K\u00fcche:", None))
        self.cbCuisine.setItemText(0, "")
        self.cbCuisine.setItemText(1, QCoreApplication.translate("dlgRecipeDB", u"African", None))
        self.cbCuisine.setItemText(2, QCoreApplication.translate("dlgRecipeDB", u"American", None))
        self.cbCuisine.setItemText(3, QCoreApplication.translate("dlgRecipeDB", u"British", None))
        self.cbCuisine.setItemText(4, QCoreApplication.translate("dlgRecipeDB", u"Cajun", None))
        self.cbCuisine.setItemText(5, QCoreApplication.translate("dlgRecipeDB", u"Caribbean", None))
        self.cbCuisine.setItemText(6, QCoreApplication.translate("dlgRecipeDB", u"Chinese", None))
        self.cbCuisine.setItemText(7, QCoreApplication.translate("dlgRecipeDB", u"Eastern European", None))
        self.cbCuisine.setItemText(8, QCoreApplication.translate("dlgRecipeDB", u"European", None))
        self.cbCuisine.setItemText(9, QCoreApplication.translate("dlgRecipeDB", u"French", None))
        self.cbCuisine.setItemText(10, QCoreApplication.translate("dlgRecipeDB", u"German", None))
        self.cbCuisine.setItemText(11, QCoreApplication.translate("dlgRecipeDB", u"Greek", None))
        self.cbCuisine.setItemText(12, QCoreApplication.translate("dlgRecipeDB", u"Indian", None))
        self.cbCuisine.setItemText(13, QCoreApplication.translate("dlgRecipeDB", u"Irish", None))
        self.cbCuisine.setItemText(14, QCoreApplication.translate("dlgRecipeDB", u"Italian", None))
        self.cbCuisine.setItemText(15, QCoreApplication.translate("dlgRecipeDB", u"Japanese", None))
        self.cbCuisine.setItemText(16, QCoreApplication.translate("dlgRecipeDB", u"Jewish", None))
        self.cbCuisine.setItemText(17, QCoreApplication.translate("dlgRecipeDB", u"Korean", None))
        self.cbCuisine.setItemText(18, QCoreApplication.translate("dlgRecipeDB", u"Latin American", None))
        self.cbCuisine.setItemText(19, QCoreApplication.translate("dlgRecipeDB", u"Mediterranean", None))
        self.cbCuisine.setItemText(20, QCoreApplication.translate("dlgRecipeDB", u"Mexican", None))
        self.cbCuisine.setItemText(21, QCoreApplication.translate("dlgRecipeDB", u"Middle Eastern", None))
        self.cbCuisine.setItemText(22, QCoreApplication.translate("dlgRecipeDB", u"Nordic", None))
        self.cbCuisine.setItemText(23, QCoreApplication.translate("dlgRecipeDB", u"Southern", None))
        self.cbCuisine.setItemText(24, QCoreApplication.translate("dlgRecipeDB", u"Spanish", None))
        self.cbCuisine.setItemText(25, QCoreApplication.translate("dlgRecipeDB", u"Thai", None))
        self.cbCuisine.setItemText(26, QCoreApplication.translate("dlgRecipeDB", u"Vietnamese", None))

        self.lbType.setText(QCoreApplication.translate("dlgRecipeDB", u"Rezept f\u00fcr:", None))
        self.cbType.setItemText(0, "")
        self.cbType.setItemText(1, QCoreApplication.translate("dlgRecipeDB", u"main course", None))
        self.cbType.setItemText(2, QCoreApplication.translate("dlgRecipeDB", u"side dish", None))
        self.cbType.setItemText(3, QCoreApplication.translate("dlgRecipeDB", u"dessert", None))
        self.cbType.setItemText(4, QCoreApplication.translate("dlgRecipeDB", u"appetizer", None))
        self.cbType.setItemText(5, QCoreApplication.translate("dlgRecipeDB", u"salad", None))
        self.cbType.setItemText(6, QCoreApplication.translate("dlgRecipeDB", u"bread", None))
        self.cbType.setItemText(7, QCoreApplication.translate("dlgRecipeDB", u"breakfast", None))
        self.cbType.setItemText(8, QCoreApplication.translate("dlgRecipeDB", u"soup", None))
        self.cbType.setItemText(9, QCoreApplication.translate("dlgRecipeDB", u"beverage", None))
        self.cbType.setItemText(10, QCoreApplication.translate("dlgRecipeDB", u"sauce", None))
        self.cbType.setItemText(11, QCoreApplication.translate("dlgRecipeDB", u"marinade", None))
        self.cbType.setItemText(12, QCoreApplication.translate("dlgRecipeDB", u"fingerfood", None))
        self.cbType.setItemText(13, QCoreApplication.translate("dlgRecipeDB", u"snack", None))
        self.cbType.setItemText(14, QCoreApplication.translate("dlgRecipeDB", u"drink", None))

        self.lbReadyTime.setText(QCoreApplication.translate("dlgRecipeDB", u"Zubereitungszeit:", None))
        self.lbMin.setText(QCoreApplication.translate("dlgRecipeDB", u"Minuten", None))
        self.lbQueryString.setText(QCoreApplication.translate("dlgRecipeDB", u"Abfrage:", None))
        self.pbDetail.setText(QCoreApplication.translate("dlgRecipeDB", u"Anzeigen", None))
    # retranslateUi

