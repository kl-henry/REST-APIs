# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogWetter_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgWetter(object):
    def setupUi(self, dlgWetter):
        if not dlgWetter.objectName():
            dlgWetter.setObjectName(u"Ui_dlgWetter")
        dlgWetter.resize(800, 800)
        dlgWetter.setStyleSheet(u"QGroupBox { background-color:  rgb(0, 255, 0); border: 3px solid rgb(255, 0, 0); }")
        self.action_Speichern = QAction(dlgWetter)
        self.action_Speichern.setObjectName(u"action_Speichern")
        self.action_Drucken = QAction(dlgWetter)
        self.action_Drucken.setObjectName(u"action_Drucken")
        self.action_Beenden = QAction(dlgWetter)
        self.action_Beenden.setObjectName(u"action_Beenden")
        self.action_Standort = QAction(dlgWetter)
        self.action_Standort.setObjectName(u"action_Standort")
        self.actionAktualisieren = QAction(dlgWetter)
        self.actionAktualisieren.setObjectName(u"actionAktualisieren")
        self.actionSonnenauf_untergang = QAction(dlgWetter)
        self.actionSonnenauf_untergang.setObjectName(u"actionSonnenauf_untergang")
        self.action_ber = QAction(dlgWetter)
        self.action_ber.setObjectName(u"action_ber")
        self.actionMin_Max_Temperatur = QAction(dlgWetter)
        self.actionMin_Max_Temperatur.setObjectName(u"actionMin_Max_Temperatur")
        self.centralwidget = QWidget(dlgWetter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 170, 395, 361))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbTemperatur = QLabel(self.layoutWidget)
        self.lbTemperatur.setObjectName(u"lbTemperatur")

        self.horizontalLayout_2.addWidget(self.lbTemperatur)

        self.lbTemperaturDisplay = QLabel(self.layoutWidget)
        self.lbTemperaturDisplay.setObjectName(u"lbTemperaturDisplay")
        self.lbTemperaturDisplay.setFrameShape(QFrame.Box)
        self.lbTemperaturDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.lbTemperaturDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbWetter = QLabel(self.layoutWidget)
        self.lbWetter.setObjectName(u"lbWetter")

        self.horizontalLayout_3.addWidget(self.lbWetter)

        self.lbWetterDisplay = QLabel(self.layoutWidget)
        self.lbWetterDisplay.setObjectName(u"lbWetterDisplay")
        self.lbWetterDisplay.setFrameShape(QFrame.Box)
        self.lbWetterDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.lbWetterDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbSonnenaufgang = QLabel(self.layoutWidget)
        self.lbSonnenaufgang.setObjectName(u"lbSonnenaufgang")

        self.horizontalLayout_5.addWidget(self.lbSonnenaufgang)

        self.lbSonnenaufgangDisplay = QLabel(self.layoutWidget)
        self.lbSonnenaufgangDisplay.setObjectName(u"lbSonnenaufgangDisplay")
        self.lbSonnenaufgangDisplay.setFrameShape(QFrame.Box)
        self.lbSonnenaufgangDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.lbSonnenaufgangDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbSonnenuntergang = QLabel(self.layoutWidget)
        self.lbSonnenuntergang.setObjectName(u"lbSonnenuntergang")

        self.horizontalLayout_4.addWidget(self.lbSonnenuntergang)

        self.lbSonnenuntergangDisplay = QLabel(self.layoutWidget)
        self.lbSonnenuntergangDisplay.setObjectName(u"lbSonnenuntergangDisplay")
        self.lbSonnenuntergangDisplay.setFrameShape(QFrame.Box)
        self.lbSonnenuntergangDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.lbSonnenuntergangDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbLuftdruck = QLabel(self.layoutWidget)
        self.lbLuftdruck.setObjectName(u"lbLuftdruck")

        self.horizontalLayout_6.addWidget(self.lbLuftdruck)

        self.lbLuftdruckDisplay = QLabel(self.layoutWidget)
        self.lbLuftdruckDisplay.setObjectName(u"lbLuftdruckDisplay")
        self.lbLuftdruckDisplay.setFrameShape(QFrame.Box)
        self.lbLuftdruckDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.lbLuftdruckDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbLuftfeuchtigkeit = QLabel(self.layoutWidget)
        self.lbLuftfeuchtigkeit.setObjectName(u"lbLuftfeuchtigkeit")

        self.horizontalLayout_7.addWidget(self.lbLuftfeuchtigkeit, 0, Qt.AlignLeft)

        self.lbLuftfeuchtigkeitDisplay = QLabel(self.layoutWidget)
        self.lbLuftfeuchtigkeitDisplay.setObjectName(u"lbLuftfeuchtigkeitDisplay")
        self.lbLuftfeuchtigkeitDisplay.setFrameShape(QFrame.Box)
        self.lbLuftfeuchtigkeitDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.lbLuftfeuchtigkeitDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbWindgeschwindigkeit = QLabel(self.layoutWidget)
        self.lbWindgeschwindigkeit.setObjectName(u"lbWindgeschwindigkeit")

        self.horizontalLayout_8.addWidget(self.lbWindgeschwindigkeit)

        self.lbWindgeschwindigkeitDisplay = QLabel(self.layoutWidget)
        self.lbWindgeschwindigkeitDisplay.setObjectName(u"lbWindgeschwindigkeitDisplay")
        self.lbWindgeschwindigkeitDisplay.setFrameShape(QFrame.Box)
        self.lbWindgeschwindigkeitDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.lbWindgeschwindigkeitDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbBewoelkung = QLabel(self.layoutWidget)
        self.lbBewoelkung.setObjectName(u"lbBewoelkung")

        self.horizontalLayout_9.addWidget(self.lbBewoelkung)

        self.lbBewoelkungDisplay = QLabel(self.layoutWidget)
        self.lbBewoelkungDisplay.setObjectName(u"lbBewoelkungDisplay")
        self.lbBewoelkungDisplay.setFrameShape(QFrame.Box)
        self.lbBewoelkungDisplay.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.lbBewoelkungDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.lbWetterIcon = QLabel(self.layoutWidget)
        self.lbWetterIcon.setObjectName(u"lbWetterIcon")
        self.lbWetterIcon.setPixmap(QPixmap(u"../../../Bilder/Icons/television_klein.png"))

        self.gridLayout.addWidget(self.lbWetterIcon, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbStand = QLabel(self.layoutWidget)
        self.lbStand.setObjectName(u"lbStand")

        self.horizontalLayout_10.addWidget(self.lbStand)

        self.lbStandDisplay = QLabel(self.layoutWidget)
        self.lbStandDisplay.setObjectName(u"lbStandDisplay")
        self.lbStandDisplay.setFrameShape(QFrame.Box)
        self.lbStandDisplay.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.lbStandDisplay)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.gbStandort = QGroupBox(self.centralwidget)
        self.gbStandort.setObjectName(u"gbStandort")
        self.gbStandort.setGeometry(QRect(30, 60, 651, 80))
        self.lbOrt = QLabel(self.gbStandort)
        self.lbOrt.setObjectName(u"lbOrt")
        self.lbOrt.setGeometry(QRect(20, 26, 71, 40))
        font = QFont()
        font.setFamily(u"Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbOrt.setFont(font)
        self.lbOrtDisplay = QLabel(self.gbStandort)
        self.lbOrtDisplay.setObjectName(u"lbOrtDisplay")
        self.lbOrtDisplay.setGeometry(QRect(70, 26, 231, 40))
        font1 = QFont()
        font1.setFamily(u"Droid Sans")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.lbOrtDisplay.setFont(font1)
        self.layoutWidget1 = QWidget(self.gbStandort)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(450, 20, 154, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbLongitude = QLabel(self.layoutWidget1)
        self.lbLongitude.setObjectName(u"lbLongitude")

        self.verticalLayout_2.addWidget(self.lbLongitude)

        self.lbLattitude = QLabel(self.layoutWidget1)
        self.lbLattitude.setObjectName(u"lbLattitude")

        self.verticalLayout_2.addWidget(self.lbLattitude)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbLongitudeDisplay = QLabel(self.layoutWidget1)
        self.lbLongitudeDisplay.setObjectName(u"lbLongitudeDisplay")

        self.verticalLayout_3.addWidget(self.lbLongitudeDisplay)

        self.lbLattitudeDisplay = QLabel(self.layoutWidget1)
        self.lbLattitudeDisplay.setObjectName(u"lbLattitudeDisplay")

        self.verticalLayout_3.addWidget(self.lbLattitudeDisplay)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(350, 610, 391, 38))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pbSpeichern = QPushButton(self.layoutWidget2)
        self.pbSpeichern.setObjectName(u"pbSpeichern")

        self.horizontalLayout_12.addWidget(self.pbSpeichern)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pbStandort = QPushButton(self.layoutWidget2)
        self.pbStandort.setObjectName(u"pbStandort")

        self.horizontalLayout_11.addWidget(self.pbStandort)

        self.pbAktualisieren = QPushButton(self.layoutWidget2)
        self.pbAktualisieren.setObjectName(u"pbAktualisieren")

        self.horizontalLayout_11.addWidget(self.pbAktualisieren)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.pbExit = QPushButton(self.layoutWidget2)
        self.pbExit.setObjectName(u"pbExit")

        self.horizontalLayout_12.addWidget(self.pbExit)

        self.gbStatistik = QGroupBox(self.centralwidget)
        self.gbStatistik.setObjectName(u"gbStatistik")
        self.gbStatistik.setGeometry(QRect(529, 160, 151, 381))
        self.pbSonnengang = QPushButton(self.gbStatistik)
        self.pbSonnengang.setObjectName(u"pbSonnengang")
        self.pbSonnengang.setGeometry(QRect(10, 40, 131, 34))
        font2 = QFont()
        font2.setPointSize(8)
        self.pbSonnengang.setFont(font2)
        self.pbTempMinMax = QPushButton(self.gbStatistik)
        self.pbTempMinMax.setObjectName(u"pbTempMinMax")
        self.pbTempMinMax.setGeometry(QRect(10, 80, 131, 34))
        self.pbTempMinMax.setFont(font2)

        self.retranslateUi(dlgWetter)
        self.pbExit.clicked.connect(dlgWetter.close)
        self.action_Beenden.triggered.connect(dlgWetter.close)
        self.pbSpeichern.clicked.connect(self.action_Speichern.trigger)
        self.pbStandort.clicked.connect(self.action_Standort.trigger)
        self.pbAktualisieren.clicked.connect(self.actionAktualisieren.trigger)
        self.pbSonnengang.clicked.connect(self.actionSonnenauf_untergang.trigger)
        self.pbTempMinMax.clicked.connect(self.actionMin_Max_Temperatur.trigger)

        QMetaObject.connectSlotsByName(dlgWetter)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("dlgWetter", u"aktuelles Wetter", None))
        self.action_Speichern.setText(QCoreApplication.translate("dlgWetter", u"&Speichern", None))
#if QT_CONFIG(shortcut)
        self.action_Speichern.setShortcut(QCoreApplication.translate("dlgWetter", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_Drucken.setText(QCoreApplication.translate("dlgWetter", u"&Drucken", None))
#if QT_CONFIG(shortcut)
        self.action_Drucken.setShortcut(QCoreApplication.translate("dlgWetter", u"Alt+D", None))
#endif // QT_CONFIG(shortcut)
        self.action_Beenden.setText(QCoreApplication.translate("dlgWetter", u"&Beenden", None))
#if QT_CONFIG(shortcut)
        self.action_Beenden.setShortcut(QCoreApplication.translate("dlgWetter", u"Alt+B", None))
#endif // QT_CONFIG(shortcut)
        self.action_Standort.setText(QCoreApplication.translate("dlgWetter", u"Stand&ort", None))
#if QT_CONFIG(tooltip)
        self.action_Standort.setToolTip(QCoreApplication.translate("dlgWetter", u"Auswahl Standort", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Standort.setShortcut(QCoreApplication.translate("dlgWetter", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAktualisieren.setText(QCoreApplication.translate("dlgWetter", u"Aktualisieren", None))
#if QT_CONFIG(shortcut)
        self.actionAktualisieren.setShortcut(QCoreApplication.translate("dlgWetter", u"Alt+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionSonnenauf_untergang.setText(QCoreApplication.translate("dlgWetter", u"Sonnenauf/untergang", None))
        self.action_ber.setText(QCoreApplication.translate("dlgWetter", u"\u00dcber", None))
        self.actionMin_Max_Temperatur.setText(QCoreApplication.translate("dlgWetter", u"Min./Max Temperatur", None))
        self.lbTemperatur.setText(QCoreApplication.translate("dlgWetter", u"Temperatur:", None))
        self.lbTemperaturDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbWetter.setText(QCoreApplication.translate("dlgWetter", u"Wetter:", None))
        self.lbWetterDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbSonnenaufgang.setText(QCoreApplication.translate("dlgWetterindow", u"Sonnenaufgang:", None))
        self.lbSonnenaufgangDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbSonnenuntergang.setText(QCoreApplication.translate("dlgWetter", u"Sonnenuntergang:", None))
        self.lbSonnenuntergangDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbLuftdruck.setText(QCoreApplication.translate("dlgWetter", u"Luftdruck:", None))
        self.lbLuftdruckDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbLuftfeuchtigkeit.setText(QCoreApplication.translate("dlgWetter", u"Luftfeuchtigkeit:", None))
        self.lbLuftfeuchtigkeitDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbWindgeschwindigkeit.setText(QCoreApplication.translate("dlgWetter", u"Wind:", None))
        self.lbWindgeschwindigkeitDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbBewoelkung.setText(QCoreApplication.translate("dlgWetter", u"Bew\u00f6lkung:", None))
        self.lbBewoelkungDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.lbWetterIcon.setText("")
        self.lbStand.setText(QCoreApplication.translate("dlgWetter", u"Stand:", None))
        self.lbStandDisplay.setText(QCoreApplication.translate("dlgWetter", u"aaa", None))
        self.gbStandort.setTitle(QCoreApplication.translate("dlgWetter", u"Standort", None))
        self.lbOrt.setText(QCoreApplication.translate("dlgWetter", u"Ort:", None))
        self.lbOrtDisplay.setText(QCoreApplication.translate("dlgWetter", u"Enkenbach-Alsenborn", None))
        self.lbLongitude.setText(QCoreApplication.translate("dlgWetter", u"geogr. L\u00e4nge:", None))
        self.lbLattitude.setText(QCoreApplication.translate("dlgWetter", u"geogr. Breite:", None))
        self.lbLongitudeDisplay.setText(QCoreApplication.translate("dlgWetter", u"TextLabel", None))
        self.lbLattitudeDisplay.setText(QCoreApplication.translate("dlgWetter", u"TextLabel", None))
        self.pbSpeichern.setText(QCoreApplication.translate("dlgWetter", u"Speichern", None))
        self.pbStandort.setText(QCoreApplication.translate("dlgWetter", u"Standort", None))
        self.pbAktualisieren.setText(QCoreApplication.translate("dlgWetter", u"Aktualisieren", None))
        self.pbExit.setText(QCoreApplication.translate("dlgWetter", u"&Ende", None))
        self.gbStatistik.setTitle(QCoreApplication.translate("dlgWetter", u"Statistik", None))
        self.pbSonnengang.setText(QCoreApplication.translate("dlgWetter", u"Sonnenauf/untergang", None))
        self.pbTempMinMax.setText(QCoreApplication.translate("dlgWetter", u"Min/Max Temperatur ", None))
    # retranslateUi

