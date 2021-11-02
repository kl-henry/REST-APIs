# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogRecipeDBDetail.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgRecipeDetails(object):
    def setupUi(self, dlgRecipeDetails):
        if not dlgRecipeDetails.objectName():
            dlgRecipeDetails.setObjectName(u"dlgRecipeDetails")
        dlgRecipeDetails.resize(1054, 670)
        self.buttonBox = QDialogButtonBox(dlgRecipeDetails)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(700, 620, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.gbUebersicht = QGroupBox(dlgRecipeDetails)
        self.gbUebersicht.setObjectName(u"gbUebersicht")
        self.gbUebersicht.setGeometry(QRect(20, 20, 491, 211))
        self.layoutWidget = QWidget(self.gbUebersicht)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 471, 161))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cbVegetarian = QCheckBox(self.layoutWidget)
        self.cbVegetarian.setObjectName(u"cbVegetarian")
        self.cbVegetarian.setEnabled(False)
        self.cbVegetarian.setLayoutDirection(Qt.RightToLeft)
        self.cbVegetarian.setCheckable(True)

        self.gridLayout.addWidget(self.cbVegetarian, 0, 0, 1, 1)

        self.cbVegan = QCheckBox(self.layoutWidget)
        self.cbVegan.setObjectName(u"cbVegan")
        self.cbVegan.setEnabled(False)
        self.cbVegan.setLayoutDirection(Qt.RightToLeft)
        self.cbVegan.setCheckable(True)

        self.gridLayout.addWidget(self.cbVegan, 0, 1, 1, 2)

        self.cbGlutenfree = QCheckBox(self.layoutWidget)
        self.cbGlutenfree.setObjectName(u"cbGlutenfree")
        self.cbGlutenfree.setEnabled(False)
        self.cbGlutenfree.setLayoutDirection(Qt.RightToLeft)
        self.cbGlutenfree.setCheckable(True)

        self.gridLayout.addWidget(self.cbGlutenfree, 0, 3, 1, 2)

        self.cbHealthy = QCheckBox(self.layoutWidget)
        self.cbHealthy.setObjectName(u"cbHealthy")
        self.cbHealthy.setEnabled(False)
        self.cbHealthy.setLayoutDirection(Qt.RightToLeft)
        self.cbHealthy.setCheckable(True)

        self.gridLayout.addWidget(self.cbHealthy, 1, 1, 1, 2)

        self.cbPopular = QCheckBox(self.layoutWidget)
        self.cbPopular.setObjectName(u"cbPopular")
        self.cbPopular.setEnabled(False)
        self.cbPopular.setLayoutDirection(Qt.RightToLeft)
        self.cbPopular.setCheckable(True)

        self.gridLayout.addWidget(self.cbPopular, 2, 0, 1, 1)

        self.cbSustainable = QCheckBox(self.layoutWidget)
        self.cbSustainable.setObjectName(u"cbSustainable")
        self.cbSustainable.setEnabled(False)
        self.cbSustainable.setLayoutDirection(Qt.RightToLeft)
        self.cbSustainable.setCheckable(True)

        self.gridLayout.addWidget(self.cbSustainable, 2, 1, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbHealthScore = QLabel(self.layoutWidget)
        self.lbHealthScore.setObjectName(u"lbHealthScore")

        self.horizontalLayout.addWidget(self.lbHealthScore)

        self.lbHealthScoreDisplay = QLabel(self.layoutWidget)
        self.lbHealthScoreDisplay.setObjectName(u"lbHealthScoreDisplay")

        self.horizontalLayout.addWidget(self.lbHealthScoreDisplay)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 3, 1, 2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbCuisines = QLabel(self.layoutWidget)
        self.lbCuisines.setObjectName(u"lbCuisines")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbCuisines)

        self.leCuisineDisplay = QLineEdit(self.layoutWidget)
        self.leCuisineDisplay.setObjectName(u"leCuisineDisplay")
        self.leCuisineDisplay.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.leCuisineDisplay)


        self.gridLayout.addLayout(self.formLayout_3, 3, 0, 1, 2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbDishType = QLabel(self.layoutWidget)
        self.lbDishType.setObjectName(u"lbDishType")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbDishType)

        self.leDishTypeDisplay = QLineEdit(self.layoutWidget)
        self.leDishTypeDisplay.setObjectName(u"leDishTypeDisplay")
        self.leDishTypeDisplay.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.leDishTypeDisplay)


        self.gridLayout.addLayout(self.formLayout_2, 3, 2, 1, 2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbDiet = QLabel(self.layoutWidget)
        self.lbDiet.setObjectName(u"lbDiet")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbDiet)

        self.leDiet = QLineEdit(self.layoutWidget)
        self.leDiet.setObjectName(u"leDiet")
        self.leDiet.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leDiet)


        self.gridLayout.addLayout(self.formLayout, 3, 4, 1, 1)

        self.cbCheap = QCheckBox(self.layoutWidget)
        self.cbCheap.setObjectName(u"cbCheap")
        self.cbCheap.setEnabled(False)
        self.cbCheap.setLayoutDirection(Qt.RightToLeft)
        self.cbCheap.setCheckable(True)

        self.gridLayout.addWidget(self.cbCheap, 1, 0, 1, 1)

        self.cbDairyProducts = QCheckBox(self.layoutWidget)
        self.cbDairyProducts.setObjectName(u"cbDairyProducts")
        self.cbDairyProducts.setEnabled(False)
        self.cbDairyProducts.setLayoutDirection(Qt.RightToLeft)
        self.cbDairyProducts.setCheckable(True)

        self.gridLayout.addWidget(self.cbDairyProducts, 1, 4, 1, 1)

        self.lbImage = QLabel(dlgRecipeDetails)
        self.lbImage.setObjectName(u"lbImage")
        self.lbImage.setGeometry(QRect(580, 70, 371, 191))
        self.lbRecipeName = QLabel(dlgRecipeDetails)
        self.lbRecipeName.setObjectName(u"lbRecipeName")
        self.lbRecipeName.setGeometry(QRect(540, 30, 61, 18))
        self.lbRecipeNameDisplay = QLabel(dlgRecipeDetails)
        self.lbRecipeNameDisplay.setObjectName(u"lbRecipeNameDisplay")
        self.lbRecipeNameDisplay.setGeometry(QRect(600, 30, 321, 18))
        self.teSummary = QTextEdit(dlgRecipeDetails)
        self.teSummary.setObjectName(u"teSummary")
        self.teSummary.setEnabled(True)
        self.teSummary.setGeometry(QRect(540, 330, 501, 261))
        self.teSummary.setFrameShape(QFrame.Box)
        self.teSummary.setUndoRedoEnabled(False)
        self.teSummary.setReadOnly(True)
        self.gbInternet = QGroupBox(dlgRecipeDetails)
        self.gbInternet.setObjectName(u"gbInternet")
        self.gbInternet.setGeometry(QRect(20, 440, 511, 151))
        self.layoutWidget1 = QWidget(self.gbInternet)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 40, 491, 48))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbOriginalURL = QLabel(self.layoutWidget1)
        self.lbOriginalURL.setObjectName(u"lbOriginalURL")

        self.verticalLayout.addWidget(self.lbOriginalURL)

        self.lbOriginalURLLink = QLabel(self.layoutWidget1)
        self.lbOriginalURLLink.setObjectName(u"lbOriginalURLLink")
        self.lbOriginalURLLink.setFrameShape(QFrame.Box)
        self.lbOriginalURLLink.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.lbOriginalURLLink)

        self.layoutWidget2 = QWidget(self.gbInternet)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 90, 491, 48))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbSpoonacularURL = QLabel(self.layoutWidget2)
        self.lbSpoonacularURL.setObjectName(u"lbSpoonacularURL")

        self.verticalLayout_2.addWidget(self.lbSpoonacularURL)

        self.lbSpoonacularURLLink = QLabel(self.layoutWidget2)
        self.lbSpoonacularURLLink.setObjectName(u"lbSpoonacularURLLink")
        self.lbSpoonacularURLLink.setFrameShape(QFrame.Box)
        self.lbSpoonacularURLLink.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.lbSpoonacularURLLink)

        self.gbUrheber = QGroupBox(dlgRecipeDetails)
        self.gbUrheber.setObjectName(u"gbUrheber")
        self.gbUrheber.setGeometry(QRect(20, 300, 511, 131))
        self.lbCreditsTextDisplay = QLabel(self.gbUrheber)
        self.lbCreditsTextDisplay.setObjectName(u"lbCreditsTextDisplay")
        self.lbCreditsTextDisplay.setGeometry(QRect(80, 60, 361, 18))
        self.lbCreditsTextDisplay.setFrameShape(QFrame.Box)
        self.lbCreditsTextDisplay.setFrameShadow(QFrame.Sunken)
        self.lbLicenseDisplay = QLabel(self.gbUrheber)
        self.lbLicenseDisplay.setObjectName(u"lbLicenseDisplay")
        self.lbLicenseDisplay.setGeometry(QRect(310, 90, 131, 18))
        self.lbLicenseDisplay.setFrameShape(QFrame.Box)
        self.lbLicenseDisplay.setFrameShadow(QFrame.Sunken)
        self.lbSourceName = QLabel(self.gbUrheber)
        self.lbSourceName.setObjectName(u"lbSourceName")
        self.lbSourceName.setGeometry(QRect(20, 90, 58, 18))
        self.lbLicense = QLabel(self.gbUrheber)
        self.lbLicense.setObjectName(u"lbLicense")
        self.lbLicense.setGeometry(QRect(240, 90, 58, 18))
        self.lbCreditsText = QLabel(self.gbUrheber)
        self.lbCreditsText.setObjectName(u"lbCreditsText")
        self.lbCreditsText.setGeometry(QRect(20, 60, 61, 18))
        self.lbQuelleDisplay = QLabel(self.gbUrheber)
        self.lbQuelleDisplay.setObjectName(u"lbQuelleDisplay")
        self.lbQuelleDisplay.setGeometry(QRect(90, 90, 131, 18))
        self.lbQuelleDisplay.setFrameShape(QFrame.Box)
        self.lbQuelleDisplay.setFrameShadow(QFrame.Sunken)
        self.lbQueryString = QLabel(dlgRecipeDetails)
        self.lbQueryString.setObjectName(u"lbQueryString")
        self.lbQueryString.setGeometry(QRect(20, 600, 58, 18))
        self.teQueryString = QTextEdit(dlgRecipeDetails)
        self.teQueryString.setObjectName(u"teQueryString")
        self.teQueryString.setGeometry(QRect(20, 620, 511, 41))
        self.teQueryString.setReadOnly(True)
        self.lbSummary = QLabel(dlgRecipeDetails)
        self.lbSummary.setObjectName(u"lbSummary")
        self.lbSummary.setGeometry(QRect(550, 300, 131, 18))

        self.retranslateUi(dlgRecipeDetails)
        self.buttonBox.accepted.connect(dlgRecipeDetails.accept)
        self.buttonBox.rejected.connect(dlgRecipeDetails.reject)

        QMetaObject.connectSlotsByName(dlgRecipeDetails)
    # setupUi

    def retranslateUi(self, dlgRecipeDetails):
        dlgRecipeDetails.setWindowTitle(QCoreApplication.translate("dlgRecipeDetails", u"Rezept Details", None))
        self.gbUebersicht.setTitle(QCoreApplication.translate("dlgRecipeDetails", u"\u00dcbersicht", None))
        self.cbVegetarian.setText(QCoreApplication.translate("dlgRecipeDetails", u"vegetarisch", None))
        self.cbVegan.setText(QCoreApplication.translate("dlgRecipeDetails", u"vegan", None))
        self.cbGlutenfree.setText(QCoreApplication.translate("dlgRecipeDetails", u"Gluten frei", None))
        self.cbHealthy.setText(QCoreApplication.translate("dlgRecipeDetails", u"sehr gesund", None))
        self.cbPopular.setText(QCoreApplication.translate("dlgRecipeDetails", u"beliebt", None))
        self.cbSustainable.setText(QCoreApplication.translate("dlgRecipeDetails", u"nachhaltig", None))
        self.lbHealthScore.setText(QCoreApplication.translate("dlgRecipeDetails", u"Gesundheits\n"
"Rating", None))
        self.lbHealthScoreDisplay.setText(QCoreApplication.translate("dlgRecipeDetails", u"aaa", None))
        self.lbCuisines.setText(QCoreApplication.translate("dlgRecipeDetails", u"K\u00fcche", None))
        self.lbDishType.setText(QCoreApplication.translate("dlgRecipeDetails", u"Gang", None))
        self.lbDiet.setText(QCoreApplication.translate("dlgRecipeDetails", u"Di\u00e4t", None))
        self.cbCheap.setText(QCoreApplication.translate("dlgRecipeDetails", u"preiswert", None))
        self.cbDairyProducts.setText(QCoreApplication.translate("dlgRecipeDetails", u"ohne\n"
"Milchprodukte", None))
        self.lbImage.setText(QCoreApplication.translate("dlgRecipeDetails", u"Image", None))
        self.lbRecipeName.setText(QCoreApplication.translate("dlgRecipeDetails", u"Name:", None))
        self.lbRecipeNameDisplay.setText(QCoreApplication.translate("dlgRecipeDetails", u"bbb", None))
        self.gbInternet.setTitle(QCoreApplication.translate("dlgRecipeDetails", u"Internet", None))
        self.lbOriginalURL.setText(QCoreApplication.translate("dlgRecipeDetails", u"Original URL:", None))
        self.lbOriginalURLLink.setText(QCoreApplication.translate("dlgRecipeDetails", u"fff", None))
        self.lbSpoonacularURL.setText(QCoreApplication.translate("dlgRecipeDetails", u"Spoonacular URL:", None))
        self.lbSpoonacularURLLink.setText(QCoreApplication.translate("dlgRecipeDetails", u"ggg", None))
        self.gbUrheber.setTitle(QCoreApplication.translate("dlgRecipeDetails", u"Urheber", None))
        self.lbCreditsTextDisplay.setText(QCoreApplication.translate("dlgRecipeDetails", u"ccc", None))
        self.lbLicenseDisplay.setText(QCoreApplication.translate("dlgRecipeDetails", u"ddd", None))
        self.lbSourceName.setText(QCoreApplication.translate("dlgRecipeDetails", u"Quelle:", None))
        self.lbLicense.setText(QCoreApplication.translate("dlgRecipeDetails", u"Lizenz:", None))
        self.lbCreditsText.setText(QCoreApplication.translate("dlgRecipeDetails", u"Home:", None))
        self.lbQuelleDisplay.setText(QCoreApplication.translate("dlgRecipeDetails", u"eee", None))
        self.lbQueryString.setText(QCoreApplication.translate("dlgRecipeDetails", u"Abfrage:", None))
        self.lbSummary.setText(QCoreApplication.translate("dlgRecipeDetails", u"Zusammenfassung:", None))
    # retranslateUi

