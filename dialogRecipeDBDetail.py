from pathlib import Path

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog

import RestAPIs_constants
import RestAPIs_utilities
from dialogRecipeDBDetail_ui import Ui_dlgRecipeDetails


class dlgWinRecipeDBDetail(QDialog, Ui_dlgRecipeDetails):
    def __init__(self, id):
        super(dlgWinRecipeDBDetail, self).__init__()
        print("dlgWinRecipeDBDetail Enter")
        self.setupUi(self)
        self.id = id
        self.recipe = ""

        self.lbSpoonacularURLLink.setOpenExternalLinks(True)
        self.lbOriginalURLLink.setOpenExternalLinks(True)
        self.lbImage.setOpenExternalLinks(True)

        self.get_recipe_detail()
        self.display_recipe_detail()

    def display_recipe_detail(self):
        # print("dlgWinRecipeDBDetail display_picture Enter")
        self.cbVegetarian.setChecked(True if str(self.recipe["vegetarian"]).capitalize() else False)
        self.cbVegan.setChecked(True if str(self.recipe["vegan"]).capitalize() else False)
        self.cbCheap.setChecked(True if str(self.recipe["cheap"]).capitalize() else False)
        self.cbGlutenfree.setChecked(True if str(self.recipe["glutenFree"]).capitalize() else False)
        self.cbDairyProducts.setChecked(True if str(self.recipe["dairyFree"]).capitalize() else False)
        self.cbHealthy.setChecked(True if str(self.recipe["veryHealthy"]).capitalize() else False)
        self.cbPopular.setChecked(True if str(self.recipe["veryPopular"]).capitalize() else False)
        self.cbSustainable.setChecked(True if str(self.recipe["sustainable"]).capitalize() else False)
        self.teSummary.insertHtml(self.recipe["summary"])
        self.lbHealthScoreDisplay.setText(str(self.recipe["healthScore"]))
        self.lbCreditsTextDisplay.setText(self.recipe["creditsText"])
        self.lbQuelleDisplay.setText(self.recipe["sourceName"])
        try:
            self.lbLicenseDisplay.setText(self.recipe["license"])
        except:
            self.lbLicenseDisplay.setText("./.")
        self.lbRecipeNameDisplay.setText(self.recipe["title"])
        self.leDishTypeDisplay.setText(self.recipe["dishTypes"][0])
        self.leCuisineDisplay.setText(self.recipe["cuisines"][0])
        if len(self.recipe["diets"]) > 0:
            self.leDiet.setText(self.recipe["diets"][0])
        else:
            self.leDiet.setText("")
        f_name = Path(self.recipe["sourceUrl"]).name
        self.lbOriginalURLLink.setText('<a href=\"' + self.recipe["sourceUrl"] + '"\>' + f_name + '</a>')
        f_name = Path(self.recipe["spoonacularSourceUrl"]).name
        self.lbSpoonacularURLLink.setText('<a href=\"' + self.recipe["spoonacularSourceUrl"] + '"\>' + f_name + '</a>')
        f_name = Path(self.recipe["image"]).name
        self.lbImage.setText('<a href=\"' + self.recipe["image"] + '"\>' + f_name + '</a>')
        # print("dlgWinRecipeDBDetail display_recipe_detail fname= ", f_name)


    def get_recipe_detail(self):
        print("dlgWinRecipeDBDetail get_recipe_detail Enter")
        # https://api.spoonacular.com/recipes/1096165/information?apiKey=79e1c8c0b27f40d9b84e492dd60903dd
        # &includeNutrition=false
        idenditification = "apiKey=" + RestAPIs_constants.SPOONACULAR_API_KEY
        query_string = "https://api.spoonacular.com/recipes/" + self.id + "/information?" \
                       + idenditification + "&" + "includeNutrition=false"
        # print("dlgWinRecipeDBDetail: get_recipe_detail, query_string= ", query_string)
        self.teQueryString.insertPlainText(query_string)
        response = RestAPIs_utilities.get_request(query_string)
        self.recipe = response.json()
        # print("dlgWinRecipeDBDetail get_recipe_detail response= ", self.recipe)

