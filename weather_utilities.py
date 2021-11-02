# -*- coding: utf-8 -*-

import json
import urllib
from urllib.error import URLError

import datetime
from urllib.request import urlopen


# with open('weatherData.json', 'r') as jsonfile:
#     weatherData = json.load(jsonfile)


def getTemperature(weatherData):
    return str(weatherData["main"]["temp"]) + " °C (gefühlt: " + getGefuehlteTemperatur(weatherData) + ")"


def get_max_Temperature(weatherData):
    return str(weatherData["main"]["temp_max"])


def get_min_Temperature(weatherData):
    return str(weatherData["main"]["temp_min"])


def getWetter(weatherData):
    return str(weatherData["weather"][0]["description"]) + " (" + getBedeckung(weatherData) + ")"


def getOrt(weatherData):
    return weatherData["name"]


def getLaenge(weatherData):
    return str(weatherData["coord"]["lon"])


def getBreite(weatherData):
    return str(weatherData["coord"]["lat"])


def getSonnenaufgangLong(weatherData):
    sunrise = datetime.datetime.fromtimestamp(weatherData["sys"]["sunrise"]).strftime("%a, %d.%b.%Y %H:%M:%S")
    return str(sunrise)


def getSonnenaufgangShort(weatherData):
    sunrise_time = datetime.datetime.fromtimestamp(weatherData["sys"]["sunrise"]).strftime("%H:%M:%S")
    sunrise_day = datetime.datetime.fromtimestamp(weatherData["sys"]["sunrise"]).date()
    return str(sunrise_time), str(sunrise_day)


def getSonnenuntergangLong(weatherData):
    sunset = datetime.datetime.fromtimestamp(weatherData["sys"]["sunset"]).strftime("%a, %d.%b.%Y %H:%M:%S")
    return str(sunset)


def getSonnenuntergangShort(weatherData):
    sunset_time = datetime.datetime.fromtimestamp(weatherData["sys"]["sunset"]).strftime("%H:%M:%S")
    sunset_day = datetime.datetime.fromtimestamp(weatherData["sys"]["sunset"]).date()
    return str(sunset_time), str(sunset_day)


def getLuftdruck(weatherData):
    return str(weatherData["main"]["pressure"]) + " hPa"


def getLuftfeuchtigkeit(weatherData):
    return str(weatherData["main"]["humidity"]) + " %"


def getGefuehlteTemperatur(weatherData):
    return str(weatherData["main"]["feels_like"]) + " °C"


def getWindgeschwindigkeit(weatherData):
    return str(weatherData["wind"]["speed"]) + " m/s, Richtung: " + getWindrichtung(weatherData)


def getBewoelkung(weatherData):
    return str(weatherData["clouds"]["all"]) + " %"


def getBedeckung(weatherData):
    return str(weatherData["weather"][0]["main"])


def getWindrichtung(weatherData):
    return str(weatherData["wind"]["deg"]) + " °"


def getAktuelleZeit(weatherData):
    # Abfragezeit
    dt = datetime.datetime.fromtimestamp(weatherData["dt"]).strftime("%a, %d.%b.%Y %H:%M:%S")
    return str(dt)

def getAktuellesDatum(weatherData):
    # Abfragezeit
    dt = datetime.datetime.fromtimestamp(weatherData["dt"]).strftime("%d.%b.%Y")
    return str(dt)


def buildSaveFileName(weatherData, ort):
    fname = "weather_data_history/" + ort + "_" + datetime.datetime.fromtimestamp(weatherData["dt"]).strftime(
        "%a_%d_%b_%Y_%H:%M:%S")
    return fname


def getWetterIcon(weatherData):
    # Wetter-Icon
    icon = weatherData["weather"][0]["icon"]
    iUrl = "http://openweathermap.org/img/w/" + icon + ".png"
    # print(iUrl)
    try:
        urllib.request.urlretrieve(iUrl, "sample.png")
    except URLError as e:
        print(e)
    return 0


def getNow():
    myNow = datetime.datetime.now()
    myHour = str(myNow.hour)
    myMinute = str(myNow.minute).rjust(2, "0")
    mySecond = str(myNow.second).rjust(2, "0")
    myTime = myHour + ":" + myMinute + ":" + mySecond
    return myTime


def getWeatherDataFromFile(fname):
    fname = "weather_data_history/" + fname
    with open(fname, 'r') as jsonfile:
        weatherData = json.load(jsonfile)
    return weatherData
