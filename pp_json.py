import json

import simplejson as simplejson

# output = '{u"visibility": 9464, u"timezone": 7200, u"main": {u"temp": 15.06, u"pressure": 1018, u"feels_like": 15.15, u"temp_max": 15.83, u"temp_min": 13.85, u"grnd_level": 987, u"humidity": 97, u"sea_level": 1018}, u"clouds": {u"all": 100}, u"sys": {u"country": u"DE", u"sunrise": 1629260642, u"type": 1, u"sunset": 1629312070, u"id": 1802}, u"dt": 1629270440, u"coord": {u"lon": 7.85, u"lat": 49.5667}, u"weather": [{u"icon": u"04d", u"description": u"Bedeckt", u"main": u"Clouds", u"id": 804}], u"name": u"Winnweiler", u"cod": 200, u"id": 2807852, u"base": u"stations", u"wind": {u"deg": 231, u"speed": 3.23, u"gust": 7.72}}'

with open('weatherData.json','r') as jsonfile:
    json_content = json.load(jsonfile)

print(json_content)

#ordered = json.loads(json_content)
#print(ordered)
# with open('weatherData.json', 'r+') as f:
#     data = json.load(f)
#     f.seek(0)
#     json.dump(data, f, indent=4)
#     f.truncate()

# weatherData = open("weatherData.json", "w")
# # magic happens here to make it pretty-printed
# weatherData.write(simplejson.dumps(simplejson.loads(output), indent=4, sort_keys=True))
# weatherData.close()
