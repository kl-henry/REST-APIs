import fnmatch
import os
import sqlite3

import weather_utilities

if __name__ == '__main__':
    fday_list = []
    orte = {"Winnweiler" : 1,
            "Enkenbach-Alsenborn" : 2,
            "Kaiserslautern": 4}

    for file in os.listdir("weather_data_history"):
        if file.endswith(".json"):
            # print(os.path.join("***weather_data_history", file))
            # print("Migrate fday ", file.split("/"))
            fday_list.append(file)
    # print("Migrate fday_list ", fday_list)
    # print("Migrate: len(fday_list) ", len(fday_list))
    id_astrodata = 0
    for fname in fday_list:
        id_astrodata += 1
        # print("type(fname)", type(fname[0]))
        weatherdata = weather_utilities.getWeatherDataFromFile(fname)
        ort = weather_utilities.getOrt(weatherdata)
        ort_id = orte[ort]
        temperature_max = weather_utilities.get_max_Temperature(weatherdata)
        # print("Temperatur aus Datei: ", temperature_max, fname)
        temperature_min = weather_utilities.get_min_Temperature(weatherdata)
        sunrise_time, sunrise_date = weather_utilities.getSonnenaufgangShort(weatherdata)
        sunset_time, sunset_date = weather_utilities.getSonnenuntergangShort(weatherdata)
        dat = weather_utilities.getAktuellesDatumRaw(weatherdata)
        # print("Migrate: ort_id ", ort_id)
        # print("Migrate: max_temp ", temperature_max)
        # print("Migrate: min_temp ", temperature_min)
        # print("Migrate: sunrise_date ", sunrise_time)
        # print("Migrate: sunrise_time ", sunrise_time)
        # print("Migrate: sunset_date ", sunrise_time)
        # print("Migrate: sunset_time ", sunset_time)
        # print("Migrate: curr_date ", dat)

        _conn = None
        sql_select_string = f"INSERT INTO astrodata (" \
                            f"fk_id_ort, min_temperature, max_temperature, " \
                            f"sunrise_date, sunrise_time, sunset_date, sunset_time, datum)" \
                            f"VALUES(?,?,?,?,?,?,?,?)"
        args = (ort_id, temperature_min, temperature_max, sunrise_date, sunrise_time, sunset_date, sunset_time, dat)
        connection_string = "weather_data_history/AstroData.db"
        try:
            _conn = sqlite3.connect(connection_string)
        except Exception as e:
            print("Error: Sqlite connection not available.\n\t%s" % e)
        cur = _conn.cursor()
        cur.execute(sql_select_string, args)
        _conn.commit()
        _conn.close()
