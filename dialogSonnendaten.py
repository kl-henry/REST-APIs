import fnmatch
import os
import re

import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as DT
from PySide2.QtWidgets import QDialog

import weather_utilities
from dialogSonne_ui import Ui_dlgSonne


class dlgWinSonne(QDialog, Ui_dlgSonne):
    def __init__(self):
        super(dlgWinSonne, self).__init__()
        self.setupUi(self)
        self.datum = ""
        self.sorted_datum = {}
        self.get_oldest_recent_dates()
        self.deVonDat.setDate(self.datum)

    def get_oldest_recent_dates(self):
        flist = fnmatch.filter(os.listdir('weather_data_history'), self.cbStandort.currentText() + '*')
        # print("dlgWinSonne get_oldest_recent_dates: ", flist, type(flist))
        # print("dlgWinSonne get_oldest_recent_dates:max(list) ", max(flist))
        daten = {}
        for fname in flist:
            dat = re.split('(\d{2}_[A-z]{3}_\d{4}_\d{2}:\d{2}:\d{2})', fname, 1)
            # print("dlgWinSonne:dat ", dat)
            datumZeit = DT.datetime.strptime(dat[1], '%d_%b_%Y_%H:%M:%S')
            daten[fname] = datumZeit
        # print("dlgWinSonne:dat ", daten)
        self.sorted_datum = dict(sorted(daten.items(), key=lambda item: item[1], reverse=True))
        # print("dlgWinSonne:sorted_datum ", self.sorted_datum)
        values_view = self.sorted_datum.values()
        value_iterator = iter(values_view)
        last_value = next(value_iterator)
        first_value = list(self.sorted_datum.keys())[-1]
        self.datum = self.sorted_datum[first_value]
        self.deBisDat.setDate(last_value)
        # print(str(self.datum) + "-" + str(self.sorted_datum[first_value]))

    def show_Sonnendaten_graph(self):
        # print("Enter show_graph")
        uniqueValues = set(self.sorted_datum.values())
        date_set = [x.date() for x in uniqueValues]
        uniqueValues = set(date_set)
        uniqueValues = sorted(uniqueValues)
        fday_list = []
        for value in uniqueValues:
            # print(value.strftime("%a_%d_%b_%Y_%H:%M:%S"))
            fday = fnmatch.filter(os.listdir('weather_data_history'),
                                  self.cbStandort.currentText() + "_" +
                                  value.strftime("%a_%d_%b_%Y") + '*')
            # print("dlgWinSonne:fday ", fday)
            fday_list.append(fday[0])
        # print("dlgWinSonne:fday_list ", fday_list)
        sunrise_time = []
        sunrise_day = []
        sunset_time = []
        sunset_day = []
        for fname in fday_list:
            weatherdata = weather_utilities.getWeatherDataFromFile(fname)
            stime, sday = weather_utilities.getSonnenaufgangShort(weatherdata)
            sunrise_time.append(stime)
            sunrise_day.append(sday)
            stime, sday = weather_utilities.getSonnenuntergangShort(weatherdata)
            sunset_time.append(stime)
            sunset_day.append(sday)
        # print("dlgWinSonne:sunrise ", sunrise_time, type(sunrise_time[0]))

        x_rise = [DT.datetime.strptime(date, "%Y-%m-%d") for date in sunrise_day]
        y_rise = [DT.datetime.strptime(time, "%H:%M:%S") for time in sunrise_time]
        x_set = [DT.datetime.strptime(date, "%Y-%m-%d") for date in sunset_day]
        y_set = [DT.datetime.strptime(time, "%H:%M:%S") for time in sunset_time]
        # print("dlgWinSonne:sunrise ", x_rise)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
        fig.suptitle('Sonnenauf/untergang in: ' + self.cbStandort.currentText())
        fig.supxlabel('Datum')
        fig.supylabel('Uhrzeit')
        # fig.tight_layout()  # sorgt für Platz zwischen den Graphs
        plt.subplots_adjust(hspace=1.0)
        # https://saralgyaan.com/posts/plot-time-series-in-python-matplotlib-tutorial-chapter-8/
        ax1.grid()
        ax2.grid()
        ax1.plot(x_rise, y_rise, 'bo-')
        ax2.plot(x_set, y_set, 'ro-')
        ax3.grid()
        ax3.plot(x_rise, y_rise, 'bo-')
        ax3.plot(x_set, y_set, 'ro-')

        myFmt = mdates.DateFormatter('%H:%M')
        x_rise_date = [date.strftime("%d.%m.%Y") for date in x_rise]
        x_set_date = [date.strftime("%d.%m.%Y") for date in x_set]

        ax1.yaxis.set_major_formatter(myFmt)
        ax1.set_title('Sonnenaufgang', fontsize=9)
        ax1.set_xticks(x_rise)
        ax1.set_xticklabels(labels=x_rise_date, fontsize=5, rotation=45)

        ax2.yaxis.set_major_formatter(myFmt)
        ax2.set_title('Sonnenuntergang', fontsize=9)
        ax2.set_xticks(x_set)
        ax2.set_xticklabels(labels=x_set_date, fontsize=5, rotation=45)

        ax3.yaxis.set_major_formatter(myFmt)

        ax3.set_xticks(x_set)
        ax3.set_xticklabels(labels=x_set_date, fontsize=5)
        # print("Ende show_graph: vor draw")

        plt.show()

    def show_Min_Max_Temperaturen_graph(self):
        # print("Enter show_Min_Max_Temperaturen_graph")
        uniqueValues = set(self.sorted_datum.values())
        date_set = [x.date() for x in uniqueValues]
        uniqueValues = set(date_set)
        uniqueValues = sorted(uniqueValues)
        fday_list = []
        for value in uniqueValues:
            print(value.strftime("%a_%d_%b_%Y_%H:%M:%S"))
            fday = fnmatch.filter(os.listdir('weather_data_history'),
                                  self.cbStandort.currentText() + "_" +
                                  value.strftime("%a_%d_%b_%Y") + '*')
            print("dlgWinSonne:fday ", fday)
            fday_list.append(fday[0])
        # print("dlgWinSonne:fday_list ", fday_list)
        max_temp = []
        min_temp = []
        curr_date = []
        for fname in fday_list:
            weatherdata = weather_utilities.getWeatherDataFromFile(fname)
            temperature = weather_utilities.get_max_Temperature(weatherdata)
            max_temp.append(temperature)
            temperature = weather_utilities.get_min_Temperature(weatherdata)
            min_temp.append(temperature)
            dat = weather_utilities.getAktuellesDatum(weatherdata)
            curr_date.append(dat)
        # print("dlgWinSonne: max_temp ", max_temp)
        # print("dlgWinSonne: min_temp ", min_temp)
        # print("dlgWinSonne: curr_date ", curr_date)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16,9))
        fig.suptitle('Min./Max Temperatur: ' + self.cbStandort.currentText())
        fig.supxlabel('Datum')
        fig.supylabel('Temperatur °C')

        plt.subplots_adjust(hspace=1.0)

        ax1.grid()
        ax2.grid()
        ax3.grid()

        max_temp_np = np.array(max_temp)
        min_temp_np = np.array(min_temp)
        curr_date_np = np.array(curr_date)

        max_value, min_value, y_ticks = self.calculate_y_axis(max_temp)
        # print(y_ticks, type(max_temp_array))
        # ax1.set_ylim(min_value, max_value)
        ax1.set_yticks(y_ticks)
        ax1.set_yticklabels(labels=y_ticks, fontsize=5)

        # print(max_temp)
        # print(min_temp)
        # print(curr_date)

        ax1.plot(curr_date, max_temp_np.astype(float), 'bo-')
        ax1.set_title('Max. Temperatur', fontsize=9)
        ax1.set_xticks(curr_date)
        ax1.set_xticklabels(labels=curr_date, fontsize=5, rotation=45)
        plt.ylim(min_value, max_value)

        ax2.plot(curr_date, min_temp_np.astype(float), 'ro-')
        ax2.set_title('Min. Temperatur', fontsize=9)
        ax2.set_xticks(curr_date)
        ax2.set_xticklabels(labels=curr_date, fontsize=5, rotation=45)
        max_value, min_value, y_ticks = self.calculate_y_axis(min_temp)
        ax2.set_yticks(y_ticks)
        ax2.set_yticklabels(labels=y_ticks, fontsize=5)
        plt.ylim(min_value, max_value)

        # print("max_temp_array, min max: ", min_value, max_value)
        ax3.plot(curr_date_np, max_temp_np.astype(float))
        ax3.plot(curr_date_np, min_temp_np.astype(float))
        ax3.set_xticks(curr_date_np)
        ax3.set_xticklabels(labels=curr_date_np, fontsize=5, rotation=45)
        temperature = min_temp + max_temp
        max_value, min_value, y_ticks = self.calculate_y_axis(temperature)
        # print("y_ticks: ", y_ticks)
        ax3.set_yticks(y_ticks)
        ax3.set_yticklabels(labels=y_ticks, fontsize=7)
        plt.ylim(min_value, max_value)
        # print("Ende show_graph: vor draw")

        plt.show()

    def calculate_y_axis(self, max_temp):
        temperature = max_temp
        temperature = np.array(temperature)
        temperature = temperature.astype(float)
        temp_array = temperature.astype(int)
        temp_array.sort()
        temp_array = np.unique(temp_array)
        min_value = min(temp_array) - 1
        max_value = max(temp_array) + 1
        y_ticks = np.linspace(min_value, max_value, max_value - min_value, endpoint=False, dtype=int)
        return max_value, min_value, y_ticks
