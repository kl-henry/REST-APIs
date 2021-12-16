import datetime
import os

from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import requests
from PySide2.QtGui import QDoubleValidator
from PySide2.QtWidgets import QDialog, QFileDialog

from RestAPIs_constants import NASA_API_KEY, HTTPS_NOT_FOUND, HTTPS_OK
from RestAPIs_utilities import show_info
from dialogLandsat_ui import Ui_dlgLandsat


class dlgWinLandsat(QDialog, Ui_dlgLandsat):
    def __init__(self):
        super(dlgWinLandsat, self).__init__()
        self.setupUi(self)
        self.dateEdit.setDate(datetime.date.today())
        self.img = None

        self.leLattitude.setValidator(QDoubleValidator(-180.0, 180.0, 2, notation=QDoubleValidator.StandardNotation))
        self.leLongitude.setValidator(QDoubleValidator(-90.0, 90.0, 2, notation=QDoubleValidator.StandardNotation))

        self.accepted.connect(self.get_image)

    def image(self,
              lat: float, lon: float, date: str = None,
              dim: float = 0.15, info: bool = False,
              api_key: str = None) -> Image.Image:
        """
        Parameters:
                lat: latitude (float)
                lon: longitude (float)
                date: date in the yyyy-mm-dd format. Defaults to most recent date (str)
                dim: width and height of image in degrees. Defaults to 0.15 (float)
                info: write onto the image the latitude and the longitude. Defaults to False (bool)
                api_key: your NASA API key (str)
        Returns:
                An Image.Image object
        """
        # print("dialogLandsat, image: lat, lon, date, dim, info", lat, lon, date, dim, info)
        if not date:
            date = datetime.now().strftime(r'%Y-%m-%d')

        payload = {
            'lat': lat,
            'lon': lon,
            'date': date,
            'dim': dim,
            'api_key': api_key,
        }
        print("dialogLandsat, image: payload", payload)
        response = requests.get(
            'https://api.nasa.gov/planetary/earth/imagery',
            params=payload,
            stream=True,
        )
        print("dialogLandsat, image: response", response.status_code)
        if response.status_code == HTTPS_NOT_FOUND:
            res = response.json()
            show_info(self, str(response.status_code), res["msg"])
        else:
            self.img = Image.open(response.raw)

            if info:
                draw = ImageDraw.Draw(self.img)
                font = ImageFont.truetype('arial.ttf', 46)
                draw.text((10, 10), f'LAT {lat}  LON {lon}', font=font, fill=(255, 0, 0))
        return response.status_code

    def get_image(self):
        print("dialogLandsat, get_image Enter")
        lat = float(self.leLattitude.text())
        lon = float(self.leLongitude.text())
        date = self.dateEdit.date().toString('yyyy-MM-dd')

        try:
            dim = float(self.leDim.text())
        except:
            dim = 0.15
        info = self.chInfo.isChecked()
        print("dialogLandsat, get_image: lat, lon, date, dim, info", lat, lon, date, dim, info)
        try:
            status = self.image(lat, lon, date, dim, info, NASA_API_KEY)
            print('dialogLandsat, get_image OK', status)
            if status == HTTPS_OK:
                self.img.show()
            # print("dialogLandsat, get_image img.filename", self.img.filename)
        except UnidentifiedImageError:
            print('Could not fetch image. Try adjusting the parameters.')


    def save_image(self):
        save = "LandSat_" + self.img.filename + ".jpg"
        try:
            self.img.save(save)
            print('Image saved successfully!')
        except ValueError:
            print('[ERROR] Unknown file extension. Image not saved!')
        except FileNotFoundError:
            print('[ERROR] Directory not found. Image not saved!')
