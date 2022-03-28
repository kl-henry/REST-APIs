# -*- coding: utf-8 -*-

import json
import sqlite3
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


def getSonnenaufgangRaw(weatherData):
    return weatherData["sys"]["sunrise"]


def getSonnenuntergangLong(weatherData):
    sunset = datetime.datetime.fromtimestamp(weatherData["sys"]["sunset"]).strftime("%a, %d.%b.%Y %H:%M:%S")
    return str(sunset)


def getSonnenuntergangShort(weatherData):
    sunset_time = datetime.datetime.fromtimestamp(weatherData["sys"]["sunset"]).strftime("%H:%M:%S")
    sunset_day = datetime.datetime.fromtimestamp(weatherData["sys"]["sunset"]).date()
    return str(sunset_time), str(sunset_day)


def getSonnenuntergangRaw(weatherData):
    return weatherData["sys"]["sunset"]


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


def getAktuellesDatumRaw(weatherData):
    # Abfragezeit
    return weatherData["dt"]


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


def get_weather_data_from_db(id_ort="Winnweiler"):
    """

    :rtype: object
    """
    orte = {"Winnweiler": 1,
            "Enkenbach-Alsenborn": 2,
            "Kaiserslautern": 4}

    _conn = None
    sql_select_string = f"select datum, temp_min, temp_max from SelectTemperaturen " \
                        f"where fk_id_ort = ?"
    connection_string = "weather_data_history/AstroData.db"
    args = [orte[id_ort]]
    try:
        _conn = sqlite3.connect(connection_string)
    except Exception as e:
        print("Error: Sqlite connection not available.\n\t%s" % e)
    cur = _conn.cursor()
    cur.execute(sql_select_string, args)
    rows = cur.fetchall()
    _conn.close()
    ret_datum = []
    ret_temp_min = []
    ret_temp_max = []
    for row in rows:
        # print("datum: ", row[0])
        # print("temp_min: ", row[1])
        # print("temp_max: ", row[2])
        # print("\n")
        ret_datum.append(row[0])
        ret_temp_min.append(row[1])
        ret_temp_max.append(row[2])
    return ret_datum, ret_temp_max, ret_temp_min


def get_sun_data_from_db(id_ort = "Winnweiler"):
    """

    :rtype: object
    """
    orte = {"Winnweiler": 1,
            "Enkenbach-Alsenborn": 2,
            "Kaiserslautern": 4}

    _conn = None
    sql_select_string = f"select Datum, Sonnenaufgang,SonnenaufgangZeit, " \
                        f"Sonnenuntergang, SonnenuntergangZeit from SelectSonnendaten " \
                        f"where fk_id_ort = ?";
    connection_string = "weather_data_history/AstroData.db"
    args = [orte[id_ort]]
    try:
        _conn = sqlite3.connect(connection_string)
    except Exception as e:
        print("Error: Sqlite connection not available.\n\t%s" % e)
    cur = _conn.cursor()
    cur.execute(sql_select_string, args)
    rows = cur.fetchall()
    _conn.close()
    ret_datum = []
    ret_sunrise = []
    ret_sunrise_time = []
    ret_sunset = []
    ret_sunset_time = []
    for row in rows:
        # print("datum: ", row[0])
        # print("ret_sunrise: ", row[1])
        # print("ret_sunset: ", row[2])
        # print("\n")
        ret_datum.append(row[0])
        ret_sunrise.append(row[1])
        ret_sunrise_time.append(row[2])
        ret_sunset.append(row[3])
        ret_sunset_time.append(row[4])
    return ret_datum, ret_sunrise, ret_sunrise_time, ret_sunset, ret_sunset_time


def save_weather_data_to_db(weatherData, id_ort="Winnweiler"):
    """

    :rtype: object
    """
    orte = {"Winnweiler": 1,
            "Enkenbach-Alsenborn": 2,
            "Kaiserslautern": 4}

    _conn = None
    sql_select_string = f"insert into astrodata (fk_id_ort, min_temperature, " \
                        f"max_temperature, sunrise_date, sunrise_time, sunset_date, sunset_time, datum)" \
                        f"VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    connection_string = "weather_data_history/AstroData.db"
    sunrise_time, sunrise_date = getSonnenaufgangShort(weatherData)
    sunset_time, sunset_date = getSonnenuntergangShort(weatherData)
    args = [orte[id_ort], float(get_min_Temperature(weatherData)), float(get_max_Temperature(weatherData)),
            sunrise_date, sunrise_time, sunset_date, sunset_time, getAktuellesDatumRaw(weatherData)]

    try:
        _conn = sqlite3.connect(connection_string)
    except Exception as e:
        print("Error: Sqlite connection not available.\n\t%s" % e)
    cur = _conn.cursor()
    cur.execute(sql_select_string, args)
    print("save_weather_data_to_db args: ", args, cur.lastrowid)
    _conn.commit()
    _conn.close()
