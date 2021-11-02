from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QDialog, QFrame

from RestAPIs_constants import keyword_switcher, FF
from RestAPIs_utilities import request_Colors, jprint, show_info
from dialogColors_ui import Ui_dlgColors


class dlgWinColors(QDialog, Ui_dlgColors):
    def __init__(self):
        super(dlgWinColors, self).__init__()

        self.setupUi(self)
        self.func_switcher = {
            "Keyword": self.execute_Keyword,
            "HEX": self.execute_HEX,
            "RGB": self.execute_RGB,
            "RGBA": self.execute_RGBA,
            "HSL": self.execute_HSL,
            "HSLA": self.execute_HSLA,
        }
        self.isAlpha = True
        self.def_color_labels_rgb = {
            "base": (self.lbColorBaseDescription, "base", "rgb", self.lbColorBase, False),
            "base_without_alpha": (self.lbColorBaseWithoutAlphaDescription, "base_without_alpha",
                                   "rgb", self.lbColorBaseWithoutAlpha, True, "base_without_alpha_contrasted_text"),
            "complementary": (
                self.lbColorComplementaryDescription, "complementary", "rgb", self.lbColorComplementary, False),
            "complementary_without_alpha": (self.lbComplementaryWithoutAlphaDescription, "complementary_without_alpha",
                                            "rgb", self.lbComplementaryWithoutAlpha, True,
                                            "complementary_without_alpha_contrasted_text"),
            "grayscale": (
                self.lbGrayScaleDescription, "grayscale", "rgb", self.lbGrayScale, False),
            "grayscale_without_alpha": (self.lbGrayScaleWithoutAlphaDescription, "grayscale_without_alpha",
                                        "rgb", self.lbGrayScaleWithoutAlpha, True,
                                        "grayscale_without_alpha_contrasted_text")
        }
        self.def_color_labels_with_alpha_rgb = {
            "base": (self.lbColorBaseDescription, "base", "rgba", self.lbColorBase, False),
            "base_without_alpha": (self.lbColorBaseWithoutAlphaDescription, "base_without_alpha",
                                   "rgb", self.lbColorBaseWithoutAlpha, True, "base_without_alpha_contrasted_text"),
            "complementary": (
                self.lbColorComplementaryDescription, "complementary", "rgba", self.lbColorComplementary, False),
            "complementary_without_alpha": (self.lbComplementaryWithoutAlphaDescription, "complementary_without_alpha",
                                            "rgb", self.lbComplementaryWithoutAlpha, True,
                                            "complementary_without_alpha_contrasted_text"),
            "grayscale": (
                self.lbGrayScaleDescription, "grayscale", "rgba", self.lbGrayScale, False),
            "grayscale_without_alpha": (self.lbGrayScaleWithoutAlphaDescription, "grayscale_without_alpha",
                                        "rgb", self.lbGrayScaleWithoutAlpha, True,
                                        "grayscale_without_alpha_contrasted_text")
        }

        self.def_color_labels_hsl = {
            "base": (self.lbColorBaseDescription, "base", "hsl_raw", self.lbColorBase, False),
            "base_without_alpha": (self.lbColorBaseWithoutAlphaDescription, "base_without_alpha",
                                   "hsl_raw", self.lbColorBaseWithoutAlpha, True, "base_without_alpha_contrasted_text"),
            "complementary": (
                self.lbColorComplementaryDescription, "complementary", "hsl_raw", self.lbColorComplementary, False),
            "complementary_without_alpha": (self.lbComplementaryWithoutAlphaDescription, "complementary_without_alpha",
                                            "hsl_raw", self.lbComplementaryWithoutAlpha, True,
                                            "complementary_without_alpha_contrasted_text"),
            "grayscale": (
                self.lbGrayScaleDescription, "grayscale", "hsl_raw", self.lbGrayScale, False),
            "grayscale_without_alpha": (self.lbGrayScaleWithoutAlphaDescription, "grayscale_without_alpha",
                                        "hsl_raw", self.lbGrayScaleWithoutAlpha, True,
                                        "grayscale_without_alpha_contrasted_text")
        }
        self.def_color_labels_with_alpha_hsl = {
            "base": (self.lbColorBaseDescription, "base", "hsla", self.lbColorBase, False),
            "base_without_alpha": (self.lbColorBaseWithoutAlphaDescription, "base_without_alpha",
                                   "hsl_raw", self.lbColorBaseWithoutAlpha, True, "base_without_alpha_contrasted_text"),
            "complementary": (
                self.lbColorComplementaryDescription, "complementary", "hsla", self.lbColorComplementary, False),
            "complementary_without_alpha": (self.lbComplementaryWithoutAlphaDescription, "complementary_without_alpha",
                                            "hsl_raw", self.lbComplementaryWithoutAlpha, True,
                                            "complementary_without_alpha_contrasted_text"),
            "grayscale": (
                self.lbGrayScaleDescription, "grayscale", "hsla", self.lbGrayScale, False),
            "grayscale_without_alpha": (self.lbGrayScaleWithoutAlphaDescription, "grayscale_without_alpha",
                                        "hsl_raw", self.lbGrayScaleWithoutAlpha, True,
                                        "grayscale_without_alpha_contrasted_text")
        }

        self.lbColorBase.setFrameShape(QFrame.Panel)
        self.lbColorBase.setFrameShadow(QFrame.Sunken)
        self.lbColorBase.setLineWidth(2)

        self.lbColorBaseWithoutAlpha.setFrameShape(QFrame.Panel)
        self.lbColorBaseWithoutAlpha.setFrameShadow(QFrame.Sunken)
        self.lbColorBaseWithoutAlpha.setLineWidth(2)

        self.lbColorComplementary.setFrameShape(QFrame.Panel)
        self.lbColorComplementary.setFrameShadow(QFrame.Sunken)
        self.lbColorComplementary.setLineWidth(2)

        self.lbComplementaryWithoutAlpha.setFrameShape(QFrame.Panel)
        self.lbComplementaryWithoutAlpha.setFrameShadow(QFrame.Sunken)
        self.lbComplementaryWithoutAlpha.setLineWidth(2)

        self.lbGrayScale.setFrameShape(QFrame.Panel)
        self.lbGrayScale.setFrameShadow(QFrame.Sunken)
        self.lbGrayScale.setLineWidth(2)

        self.lbGrayScaleWithoutAlpha.setFrameShape(QFrame.Panel)
        self.lbGrayScaleWithoutAlpha.setFrameShadow(QFrame.Sunken)
        self.lbGrayScaleWithoutAlpha.setLineWidth(2)

        self.gbColorDisplay.setStyleSheet("QGroupBox { background-color: rgb(255, 255, 255); \
                                                border: 3px solid rgb(255, 0, 0); }")

        self.cbColorFormat.currentTextChanged.connect(self.on_combobox_changed)
        self.pbRequest.clicked.connect(self.get_Colors)

    def get_Colors(self):
        # print("dlgWinColors get_Colors: Enter")
        func = self.func_switcher.get(self.cbColorFormat.currentText())
        func()

    def execute_API(self, col_string=None, alpha=False):
        # print("dlgWinColors execute_API: Enter", col_string)
        status, response = request_Colors(col_string)
        # print("execute_API: ", response["status"])
        if response["status"] == "success":
            # print("execute_Keyword success")
            # jprint(response)
            # with open("test_colors_1.json", 'w') as outfile:
            #     json.dump(response, outfile)
            print("execute_API: ", self.cbColorFormat.currentText()+" "+ str(alpha))
            if alpha:
                if self.cbColorFormat.currentText() == "HSL":
                    self.process_color_data(response, self.def_color_labels_with_alpha_hsl)
                else:
                    print("execute_API: if alpha and HSL else")
                    self.process_color_data(response, self.def_color_labels_with_alpha_rgb)
            else:
                if self.cbColorFormat.currentText() == "HSLA":
                    self.process_color_data(response, self.def_color_labels_hsl)
                else:
                    print("execute_API: ", response)
                    self.process_color_data(response, self.def_color_labels_rgb)
        else:
            # print("execute_Keyword: ", response["status"], response["error"]["type"],
            # response["error"]["value"]
            #       + ": " + response["error"]["message"])
            show_info(self, winTitle=response["error"]["type"],
                      winInfo=response["error"]["value"] + ": " + response["error"]["message"])

    def process_color_data(self, response, dict_to_use):
        for item in dict_to_use:
            # print(type(item), item)
            # print(self.def_color_labels[item][1])
            lbText = self.def_color_labels_rgb[item][1]
            # TODO ergänze ALPHA Varianten
            dict_to_use[item][0].setText(
                lbText + ": " + response[dict_to_use[item][1]]["keyword"] + " "
                + response[dict_to_use[item][1]][dict_to_use[item][2]]["value"])

            # print("style_string: ", style_string)
            if dict_to_use[item][4]:
                dict_to_use[item][3].setText("Komplementär: "
                                             + response[dict_to_use[item][5]][dict_to_use[item][2]]["value"])
                style_string = "background-color: " + response[dict_to_use[item][1]][dict_to_use[item][2]]["value"] \
                               + ";" + "color: " + response[dict_to_use[item][5]][dict_to_use[item][2]]["value"] + ";"
            else:
                dict_to_use[item][3].setText("")
                style_string = "background-color: " + response[dict_to_use[item][1]][dict_to_use[item][2]]["value"]+";"
            dict_to_use[item][3].setStyleSheet(style_string)

    def execute_Keyword(self):
        # print("dlgWinColors execute_Keyword: Enter")
        col_string = self.leColorCode.text()
        colorFormat = self.cbColorFormat.currentText()
        col_string = keyword_switcher.get(colorFormat) + col_string
        # print("execute_Keyword: col_string = ", col_string)
        self.execute_API(col_string=col_string)

    def execute_HEX(self):
        # print("dlgWinColors execute_HEX: Enter")
        color_code = self.leColorCode.text()
        color_code_hex = int(round(int(self.sbAlpha.text()) * 255 / 100, 0))
        color_code_hex = f'{color_code_hex:02x}'
        color_code = color_code + color_code_hex
        # print("dlgWinColors execute_HEX, color_code: ", color_code)
        if len(color_code) > 8:
            self.show_info(self, "Fehler", "zu viele Zeichen")
        else:
            col_string = keyword_switcher.get("HEX") + color_code
            print("dlgWinColors execute_HEX, col_string: ", col_string)
            self.execute_API(col_string=col_string, alpha=False if (color_code_hex == FF) else True)

    def execute_RGB(self):
        # print("dlgWinColors execute_RGB: Enter")
        color_code = self.leColorCode.text()
        # print("dlgWinColors execute_RGB: color_code", color_code)
        rgb_parms = color_code.split(',')
        # print("dlgWinColors execute_RGB: rgb_parms", rgb_parms[1])
        col_code = "{0},{1},{2}".format(int(rgb_parms[0]), int(rgb_parms[1]), int(rgb_parms[2]))
        # print("dlgWinColors execute_RGB: col_code", col_code)
        col_string = keyword_switcher.get(self.cbColorFormat.currentText()) + col_code
        # print("dlgWinColors execute_RGB: col_string", col_string)
        self.execute_API(col_string=col_string, alpha=False)

    def execute_RGBA(self):
        # print("dlgWinColors execute_RGBA: Enter")
        color_code = self.leColorCode.text()
        color_code_hex = round(int(self.sbAlpha.text()) / 100, 2)
        # print("dlgWinColors execute_RGBA: color_code_hex", color_code_hex)
        rgb_parms = color_code.split(',')
        # print("dlgWinColors execute_RGBA: rgb_parms", rgb_parms[1])
        col_code = "{0},{1},{2}".format(int(rgb_parms[0]), int(rgb_parms[1]), int(rgb_parms[2]))
        # print("dlgWinColors execute_RGBA: col_code", col_code)
        col_string = keyword_switcher.get(self.cbColorFormat.currentText()) + col_code + "," + \
                     "{0:.2f}".format(color_code_hex)
        # print("dlgWinColors execute_RGBA: col_string", col_string)
        self.execute_API(col_string=col_string, alpha=True)

    def execute_HSL(self):
        print("dlgWinColors execute_HSL: Enter")
        color_code = self.leColorCode.text()
        # print("dlgWinColors execute_HSL: color_code", color_code)
        rgb_parms = color_code.split(',')
        # print("dlgWinColors execute_HSL: rgb_parms", rgb_parms[1])
        col_code = "{0},{1},{2}".format(int(rgb_parms[0]), int(rgb_parms[1]), int(rgb_parms[2]))
        # print("dlgWinColors execute_HSL: col_code", col_code)
        col_string = keyword_switcher.get(self.cbColorFormat.currentText()) + col_code
        print("dlgWinColors execute_HSL: col_string", col_string)
        self.execute_API(col_string=col_string, alpha=False)

    def execute_HSLA(self):
        print("dlgWinColors execute_HSLA: Enter")
        color_code = self.leColorCode.text()
        color_code_hex = round(int(self.sbAlpha.text()) / 100, 2)
        # print("dlgWinColors execute_HSLA: color_code_hex", color_code_hex)
        rgb_parms = color_code.split(',')
        # print("dlgWinColors execute_HSLA: rgb_parms", rgb_parms[1])
        col_code = "{0},{1},{2}".format(int(rgb_parms[0]), int(rgb_parms[1]), int(rgb_parms[2]))
        # print("dlgWinColors execute_HSLA: col_code", col_code)
        col_string = keyword_switcher.get(self.cbColorFormat.currentText()) + col_code + "," + \
                     "{0:.2f}".format(color_code_hex)
        print("dlgWinColors execute_HSLA: col_string", col_string)
        self.execute_API(col_string=col_string, alpha=False if color_code_hex == FF else True)

    def on_combobox_changed(self):
        if self.cbColorFormat.currentText() == "HEX":
            validator = QRegExpValidator(QRegExp("[0-9A-Fa-f]{6}"))
            self.leColorCode.setValidator(validator)
        elif self.cbColorFormat.currentText() in ["RGB", "RGBA"]:
            self.leColorCode.setToolTip("Einagbeformat: xyz,xyz,xyz")
            ipRange = "(255|[-+]?[0-9]{1,3})"  # Part of the regular expression
            # Regulare expression
            ipRegex = QRegExp(ipRange + "\\," + ipRange + "\\," + ipRange)
            input_validator = QRegExpValidator(ipRegex, self.leColorCode)
            self.leColorCode.setValidator(input_validator)
        elif self.cbColorFormat.currentText() in ["HSL", "HSLA"]:
            self.leColorCode.setToolTip("Einagbeformat: Hue(0-255),Saturation(0-100),Lightness(0-100)")
            ipRange = "(255|[-+]?[0-9]{1,3})"  # Part of the regular expression
            # Regulare expression
            ipRegex = QRegExp(ipRange + "\\," + ipRange + "\\," + ipRange)
            input_validator = QRegExpValidator(ipRegex, self.leColorCode)
            self.leColorCode.setValidator(input_validator)
        else:
            self.leColorCode.setToolTip("")
            validator = QRegExpValidator(QRegExp(".*"))
            self.leColorCode.setValidator(validator)
