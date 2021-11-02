# -*- coding: utf-8 -*-
import datetime
import json

import urllib3
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *
from bs4 import BeautifulSoup

# import weather_utilities
from dialogSonnendaten import dlgWinSonne
from dialogStandort import dlgWinStandort
import weather_utilities
from dialogWetter_ui import Ui_dlgWetter
from weather_utilities import getTemperature


class dlgWinWetter(QDialog, Ui_dlgWetter):
    def __init__(self):
        super(dlgWinWetter, self).__init__()
        self.setupUi(self)
        self.weatherData = ""
        self.ort = ""

        self.action_Speichern.triggered.connect(self.daten_speichern)
        self.action_Standort.triggered.connect(self.auswahl_standort)
        self.actionAktualisieren.triggered.connect(self.standort_aktualisieren)
        self.actionSonnenauf_untergang.triggered.connect(self.select_Sonnendaten)
        self.actionMin_Max_Temperatur.triggered.connect(self.select_Min_Max_Temperaturen)

        self.gbStatistik.setStyleSheet("QGroupBox { background-color: rgb(255, 255, 255); \
                                        border: 3px solid rgb(255, 0, 0); }")

        self.lbOrtDisplay.setText("Winnweiler")
        self.show()
        self.getLiveData(self.lbOrtDisplay.text())
        self.populate_Labels()

    def populate_Labels(self):
        self.lbTemperaturDisplay.setText(getTemperature(self.weatherData))
        self.lbWetterDisplay.setText(weather_utilities.getWetter(self.weatherData))
        self.lbOrtDisplay.setText(weather_utilities.getOrt(self.weatherData))
        self.lbLattitudeDisplay.setText(weather_utilities.getBreite(self.weatherData))
        self.lbLongitudeDisplay.setText(weather_utilities.getLaenge(self.weatherData))
        self.lbSonnenaufgangDisplay.setText(weather_utilities.getSonnenaufgangLong(self.weatherData))
        self.lbSonnenuntergangDisplay.setText(weather_utilities.getSonnenuntergangLong(self.weatherData))
        self.lbLuftdruckDisplay.setText(weather_utilities.getLuftdruck(self.weatherData))
        self.lbLuftfeuchtigkeitDisplay.setText(weather_utilities.getLuftfeuchtigkeit(self.weatherData))
        self.lbWindgeschwindigkeitDisplay.setText(weather_utilities.getWindgeschwindigkeit(self.weatherData))
        self.lbBewoelkungDisplay.setText(weather_utilities.getBewoelkung(self.weatherData))
        self.lbStandDisplay.setText(weather_utilities.getAktuelleZeit(self.weatherData))

        weather_utilities.getWetterIcon(self.weatherData)
        self.lbWetterIcon.setPixmap("sample.png")

    def getLiveData(self, ort):
        weatherUrl = "http://api.openweathermap.org/data/2.5/weather?" + \
                     "q=" + ort + ",DE&units=metric&lang=de&APPID=1fc63a784b9e19138f2e3b40792889fc"
        # print(weatherUrl)
        http = urllib3.PoolManager()
        response = http.request('GET', weatherUrl)
        soup = BeautifulSoup(response.data.decode('utf-8'), features="html.parser")
        weatherData = json.loads(str(soup))
        # print(weatherData)
        self.weatherData = weatherData

    def daten_speichern(self):
        # print("Daten Speichern gewählt")
        fname = weather_utilities.buildSaveFileName(self.weatherData, self.lbOrtDisplay.text()) + ".json"
        # print(fname)
        with open(fname, 'w') as json_file:
            json.dump(self.weatherData, json_file)

    def auswahl_standort(self):
        dlgWin = dlgWinStandort()
        result = dlgWin.exec_()
        # print(result)
        if result:
            # print("Standort: " + dlgWin.leStandort.text())
            self.ort = dlgWin.cbStandort.currentText()
            self.getLiveData(self.ort)
            if self.weatherData["cod"] == '404':
                QMessageBox.information(self, 'Standort Auswahl', "Standort nicht gefunden: \n" + self.ort,
                                        QMessageBox.Yes)
            else:
                self.lbOrtDisplay.setText(self.ort)
                self.standort_aktualisieren()
        # print(dlgWin.cbStandort.currentText())

    def standort_aktualisieren(self):
        # print("Enter standort_aktualisieren")
        self.statusbar.showMessage("Daten werden aktualisiert...")
        self.getLiveData(self.lbOrtDisplay.text())
        self.populate_Labels()
        self.statusbar.clearMessage()

    def select_Sonnendaten(self):
        # print("Enter select_Sonnendaten")
        dlgWin = dlgWinSonne()
        result = dlgWin.exec_()
        if result:
            # print("select_Sonnendaten", result)
            dlgWin.get_oldest_recent_dates()
            dlgWin.show_Sonnendaten_graph()
        else:
            print("Kein Graph ausgewählt", result)

    def select_Min_Max_Temperaturen(self):
        # print("Enter select_Min_Max_Temperaturen")
        dlgWin = dlgWinSonne()
        result = dlgWin.exec_()
        if result:
            # print("select_Min_Max_Temperaturen", result)
            dlgWin.get_oldest_recent_dates()
            dlgWin.show_Min_Max_Temperaturen_graph()
        else:
            print("Kein Graph ausgewählt", result)
