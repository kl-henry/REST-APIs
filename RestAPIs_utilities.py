import json
import urllib
from datetime import datetime
from urllib.error import URLError

import requests
from PySide2.QtWidgets import QMessageBox, QFileDialog
import nasapy

from RestAPIs_constants import NASA_API_KEY


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def jprint_to_file(jsonFilename, jsonData):
    with open(jsonFilename, 'w') as outfile:
        json.dump(jsonData, outfile, sort_keys=True, indent=4)


def get_request(url):
    # print("get_request: ", url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


def getImageFile(url, partName):
    print(url)
    fname = buildFileName(partName)
    try:
        urllib.request.urlretrieve(url, fname)
    except URLError as e:
        print(e)
    return fname


def buildFileName(partName):
    return "data/" + partName + "_" + datetime.now().strftime("%Y_%m_%d") + ".png"


def request_xkcd():
    # Use a breakpoint in the code line below to debug your script.
    res = get_request("https://xkcd.com/info.0.json")
    # print(res.status_code, type(res.status_code))
    return res.status_code, res.json()


def request_Astros():
    # Use a breakpoint in the code line below to debug your script.
    res = get_request("http://api.open-notify.org/astros.json")
    # print(res.status_code, type(res.status_code))
    # jprint(res.json())
    return res.status_code, res.json()


def request_Lyrics(artist, title):
    # print ("request_Lyrics: ", artist, title)
    res = get_request("https://api.lyrics.ovh/v1/" + artist + "/" + title)
    # print(res.status_code, type(res.status_code))
    # jprint(res.json())
    return res.status_code, res.json()


def request_Bored():
    # print ("request_Bored: Enter")
    res = get_request("http://www.boredapi.com/api/activity/")
    # jprint(res.json())
    return res.status_code, res.json()


def request_Colors(keyword_color):
    # print ("request_Bored: Enter")
    url = "https://color.serialif.com/" + keyword_color
    res = get_request(url)
    # jprint(res.json())
    return res.status_code, res.json()


def show_info(self, winTitle="Info", winInfo="This is Information"):
    QMessageBox.information(self, winTitle, winInfo)


def load_apod(self):
    # print("RESTAPIs_utilities load_apod Enter")
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filters = ".jpg (*.jpg *.JPG)"
    title = "Import NASA APOD Picture"
    open_at = "/home/heinz/Dokumente/Hintergrundbilder"
    data = QFileDialog.getOpenFileName(None, title, open_at, filters, options=options)

    # print("RESTAPIs_utilities load_apod: fname= ", data[0])
    # print("RESTAPIs_utilities load_apod: fname= ", data[0])

    return data


def request_RecipeDB(title):
    print("request_RecipeDB: ", title)

    request_string = "http://www.omdbapi.com/" + title
    res = get_request(request_string)
    # print(res.status_code, type(res.status_code))
    jprint(res.json())
    return res


def create_nasa_instance():
    k = NASA_API_KEY
    return nasapy.Nasa(key=k)
