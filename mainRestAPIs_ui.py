# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(536, 520)
        self.actionBeenden = QAction(MainWindow)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.actionXkcd = QAction(MainWindow)
        self.actionXkcd.setObjectName(u"actionXkcd")
        self.actionAstros = QAction(MainWindow)
        self.actionAstros.setObjectName(u"actionAstros")
        self.action_ber = QAction(MainWindow)
        self.action_ber.setObjectName(u"action_ber")
        self.actionLyrics = QAction(MainWindow)
        self.actionLyrics.setObjectName(u"actionLyrics")
        self.actionBored = QAction(MainWindow)
        self.actionBored.setObjectName(u"actionBored")
        self.actionColors = QAction(MainWindow)
        self.actionColors.setObjectName(u"actionColors")
        self.actionWetter = QAction(MainWindow)
        self.actionWetter.setObjectName(u"actionWetter")
        self.actionGetApod = QAction(MainWindow)
        self.actionGetApod.setObjectName(u"actionGetApod")
        self.actionNasaEpic = QAction(MainWindow)
        self.actionNasaEpic.setObjectName(u"actionNasaEpic")
        self.actionMarsRoverPictures = QAction(MainWindow)
        self.actionMarsRoverPictures.setObjectName(u"actionMarsRoverPictures")
        self.actionRecipeDB = QAction(MainWindow)
        self.actionRecipeDB.setObjectName(u"actionRecipeDB")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gbScience = QGroupBox(self.centralwidget)
        self.gbScience.setObjectName(u"gbScience")
        self.gbScience.setGeometry(QRect(40, 20, 371, 121))
        self.gbScience.setStyleSheet(u"QGroupBox { background-color: rgb(255, 255, 255);  border: 3px solid rgb(255, 0, 0); }")
        self.pbAstros = QPushButton(self.gbScience)
        self.pbAstros.setObjectName(u"pbAstros")
        self.pbAstros.setGeometry(QRect(20, 40, 51, 51))
        self.pbAstros.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u"../../../Bilder/Icons/icons8-astronaut-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbAstros.setIcon(icon)
        self.pbWetter = QPushButton(self.gbScience)
        self.pbWetter.setObjectName(u"pbWetter")
        self.pbWetter.setGeometry(QRect(80, 40, 51, 51))
        self.pbWetter.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"../../../Bilder/Icons/icons8-sonne-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbWetter.setIcon(icon1)
        self.pbApod = QPushButton(self.gbScience)
        self.pbApod.setObjectName(u"pbApod")
        self.pbApod.setGeometry(QRect(140, 40, 51, 51))
        self.pbApod.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u"../../../Bilder/Icons/observatory.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbApod.setIcon(icon2)
        self.pbEpic = QPushButton(self.gbScience)
        self.pbEpic.setObjectName(u"pbEpic")
        self.pbEpic.setGeometry(QRect(200, 40, 51, 51))
        self.pbEpic.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u"../../../Bilder/Icons/icons8-europa-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbEpic.setIcon(icon3)
        self.pbMarsRoverPictures = QPushButton(self.gbScience)
        self.pbMarsRoverPictures.setObjectName(u"pbMarsRoverPictures")
        self.pbMarsRoverPictures.setGeometry(QRect(260, 40, 51, 51))
        self.pbMarsRoverPictures.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u"../../../Bilder/Icons/icons8-mars-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMarsRoverPictures.setIcon(icon4)
        self.pbEnde = QPushButton(self.centralwidget)
        self.pbEnde.setObjectName(u"pbEnde")
        self.pbEnde.setGeometry(QRect(400, 420, 88, 34))
        self.gbDevelopment = QGroupBox(self.centralwidget)
        self.gbDevelopment.setObjectName(u"gbDevelopment")
        self.gbDevelopment.setGeometry(QRect(40, 170, 201, 121))
        self.gbDevelopment.setStyleSheet(u"QGroupBox { background-color: rgb(255, 255, 255);  border: 3px solid rgb(255, 0, 0); }")
        self.pbColors = QPushButton(self.gbDevelopment)
        self.pbColors.setObjectName(u"pbColors")
        self.pbColors.setGeometry(QRect(20, 30, 51, 51))
        self.pbColors.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"../../../Bilder/Icons/icons8-colors-58.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbColors.setIcon(icon5)
        self.gbFun = QGroupBox(self.centralwidget)
        self.gbFun.setObjectName(u"gbFun")
        self.gbFun.setGeometry(QRect(40, 310, 331, 121))
        self.gbFun.setStyleSheet(u"QGroupBox { background-color: rgb(255, 255, 255);  border: 3px solid rgb(255, 0, 0); }")
        self.pbBored = QPushButton(self.gbFun)
        self.pbBored.setObjectName(u"pbBored")
        self.pbBored.setGeometry(QRect(20, 40, 51, 51))
        icon6 = QIcon()
        icon6.addFile(u"../../../Bilder/Icons/icons8-bmo-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbBored.setIcon(icon6)
        self.pbXKCD = QPushButton(self.gbFun)
        self.pbXKCD.setObjectName(u"pbXKCD")
        self.pbXKCD.setGeometry(QRect(90, 40, 51, 51))
        icon7 = QIcon()
        icon7.addFile(u"../../../Bilder/Icons/television_klein.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbXKCD.setIcon(icon7)
        self.pbLyrics = QPushButton(self.gbFun)
        self.pbLyrics.setObjectName(u"pbLyrics")
        self.pbLyrics.setGeometry(QRect(160, 40, 51, 51))
        self.pbLyrics.setLayoutDirection(Qt.LeftToRight)
        icon8 = QIcon()
        icon8.addFile(u"../../../Bilder/Icons/icons8-gesangslehrer-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbLyrics.setIcon(icon8)
        self.pbRecipeDB = QPushButton(self.gbFun)
        self.pbRecipeDB.setObjectName(u"pbRecipeDB")
        self.pbRecipeDB.setGeometry(QRect(230, 40, 51, 51))
        self.pbRecipeDB.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u"../../../Bilder/Icons/icons8-recipe-book-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbRecipeDB.setIcon(icon9)
        self.pbRecipeDB.setIconSize(QSize(51, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 536, 30))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuPublic_REST_APIs = QMenu(self.menubar)
        self.menuPublic_REST_APIs.setObjectName(u"menuPublic_REST_APIs")
        self.menuHilfe = QMenu(self.menubar)
        self.menuHilfe.setObjectName(u"menuHilfe")
        self.menuDevelopment = QMenu(self.menubar)
        self.menuDevelopment.setObjectName(u"menuDevelopment")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuPublic_REST_APIs.menuAction())
        self.menubar.addAction(self.menuDevelopment.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())
        self.menuDatei.addAction(self.actionBeenden)
        self.menuPublic_REST_APIs.addAction(self.actionXkcd)
        self.menuPublic_REST_APIs.addAction(self.actionAstros)
        self.menuHilfe.addAction(self.action_ber)
        self.menuDevelopment.addAction(self.actionBored)
        self.menuDevelopment.addAction(self.actionColors)

        self.retranslateUi(MainWindow)
        self.pbEnde.clicked.connect(MainWindow.close)
        self.pbXKCD.clicked.connect(self.actionXkcd.trigger)
        self.actionBeenden.triggered.connect(MainWindow.close)
        self.pbAstros.clicked.connect(self.actionAstros.trigger)
        self.pbLyrics.clicked.connect(self.actionLyrics.trigger)
        self.pbBored.clicked.connect(self.actionBored.trigger)
        self.pbColors.clicked.connect(self.actionColors.trigger)
        self.pbWetter.clicked.connect(self.actionWetter.trigger)
        self.pbApod.clicked.connect(self.actionGetApod.trigger)
        self.pbEpic.clicked.connect(self.actionNasaEpic.trigger)
        self.pbMarsRoverPictures.clicked.connect(self.actionMarsRoverPictures.trigger)
        self.pbRecipeDB.clicked.connect(self.actionRecipeDB.trigger)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionBeenden.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
        self.actionXkcd.setText(QCoreApplication.translate("MainWindow", u"Xkcd", None))
        self.actionAstros.setText(QCoreApplication.translate("MainWindow", u"Astros", None))
        self.action_ber.setText(QCoreApplication.translate("MainWindow", u"\u00dcber", None))
        self.actionLyrics.setText(QCoreApplication.translate("MainWindow", u"Lyrics", None))
#if QT_CONFIG(tooltip)
        self.actionLyrics.setToolTip(QCoreApplication.translate("MainWindow", u"Suche Songtexte", None))
#endif // QT_CONFIG(tooltip)
        self.actionBored.setText(QCoreApplication.translate("MainWindow", u"Bored", None))
#if QT_CONFIG(tooltip)
        self.actionBored.setToolTip(QCoreApplication.translate("MainWindow", u"Activities to do when Bored", None))
#endif // QT_CONFIG(tooltip)
        self.actionColors.setText(QCoreApplication.translate("MainWindow", u"Colors", None))
#if QT_CONFIG(tooltip)
        self.actionColors.setToolTip(QCoreApplication.translate("MainWindow", u"Convert Colorcodes", None))
#endif // QT_CONFIG(tooltip)
        self.actionWetter.setText(QCoreApplication.translate("MainWindow", u"Wetter", None))
#if QT_CONFIG(tooltip)
        self.actionWetter.setToolTip(QCoreApplication.translate("MainWindow", u"akt. Wetter", None))
#endif // QT_CONFIG(tooltip)
        self.actionGetApod.setText(QCoreApplication.translate("MainWindow", u"getApod", None))
#if QT_CONFIG(tooltip)
        self.actionGetApod.setToolTip(QCoreApplication.translate("MainWindow", u"APOD from NASA", None))
#endif // QT_CONFIG(tooltip)
        self.actionNasaEpic.setText(QCoreApplication.translate("MainWindow", u"NasaEpic", None))
#if QT_CONFIG(tooltip)
        self.actionNasaEpic.setToolTip(QCoreApplication.translate("MainWindow", u"EPIC(Earth Polychromatic Imaging Camera) from NASA", None))
#endif // QT_CONFIG(tooltip)
        self.actionMarsRoverPictures.setText(QCoreApplication.translate("MainWindow", u"MarsRoverPictures", None))
#if QT_CONFIG(tooltip)
        self.actionMarsRoverPictures.setToolTip(QCoreApplication.translate("MainWindow", u"Get Mars Rover Pictures", None))
#endif // QT_CONFIG(tooltip)
        self.actionRecipeDB.setText(QCoreApplication.translate("MainWindow", u"RecipeDB", None))
#if QT_CONFIG(tooltip)
        self.actionRecipeDB.setToolTip(QCoreApplication.translate("MainWindow", u"Rezepte suchen", None))
#endif // QT_CONFIG(tooltip)
        self.gbScience.setTitle(QCoreApplication.translate("MainWindow", u"Wissenschaft", None))
#if QT_CONFIG(tooltip)
        self.pbAstros.setToolTip(QCoreApplication.translate("MainWindow", u"akt. Raumfahrer anzeigen", None))
#endif // QT_CONFIG(tooltip)
        self.pbAstros.setText("")
#if QT_CONFIG(tooltip)
        self.pbWetter.setToolTip(QCoreApplication.translate("MainWindow", u"akt. Wetter", None))
#endif // QT_CONFIG(tooltip)
        self.pbWetter.setText("")
#if QT_CONFIG(tooltip)
        self.pbApod.setToolTip(QCoreApplication.translate("MainWindow", u"APOD from NASA", None))
#endif // QT_CONFIG(tooltip)
        self.pbApod.setText("")
#if QT_CONFIG(tooltip)
        self.pbEpic.setToolTip(QCoreApplication.translate("MainWindow", u"EPIC(Earth Polychromatic Imaging Camera) from NASA", None))
#endif // QT_CONFIG(tooltip)
        self.pbEpic.setText("")
#if QT_CONFIG(tooltip)
        self.pbMarsRoverPictures.setToolTip(QCoreApplication.translate("MainWindow", u"Get Mars Rover Pictures", None))
#endif // QT_CONFIG(tooltip)
        self.pbMarsRoverPictures.setText("")
        self.pbEnde.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
        self.gbDevelopment.setTitle(QCoreApplication.translate("MainWindow", u"Development", None))
#if QT_CONFIG(tooltip)
        self.pbColors.setToolTip(QCoreApplication.translate("MainWindow", u"Convert Colors", None))
#endif // QT_CONFIG(tooltip)
        self.pbColors.setText("")
        self.gbFun.setTitle(QCoreApplication.translate("MainWindow", u"Spa\u00df", None))
#if QT_CONFIG(tooltip)
        self.pbBored.setToolTip(QCoreApplication.translate("MainWindow", u"Things to do when bored", None))
#endif // QT_CONFIG(tooltip)
        self.pbBored.setText("")
#if QT_CONFIG(tooltip)
        self.pbXKCD.setToolTip(QCoreApplication.translate("MainWindow", u"XKCD Comic", None))
#endif // QT_CONFIG(tooltip)
        self.pbXKCD.setText("")
#if QT_CONFIG(tooltip)
        self.pbLyrics.setToolTip(QCoreApplication.translate("MainWindow", u"Songtexte", None))
#endif // QT_CONFIG(tooltip)
        self.pbLyrics.setText("")
#if QT_CONFIG(tooltip)
        self.pbRecipeDB.setToolTip(QCoreApplication.translate("MainWindow", u"Rezepte suchen", None))
#endif // QT_CONFIG(tooltip)
        self.pbRecipeDB.setText("")
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuPublic_REST_APIs.setTitle(QCoreApplication.translate("MainWindow", u"Public REST APIs", None))
        self.menuHilfe.setTitle(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.menuDevelopment.setTitle(QCoreApplication.translate("MainWindow", u"Development", None))
    # retranslateUi
