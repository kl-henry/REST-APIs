import json

from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import SIGNAL, QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QDialog, QListWidgetItem, QAbstractItemView

import RestAPIs_constants
import RestAPIs_utilities
from RestAPIs_constants import OMDB_API_KEY
from RestAPIs_utilities import request_RecipeDB
from dialogRecipeDBDetail import dlgWinRecipeDBDetail
from dialogRecipeDB_ui import Ui_dlgRecipeDB


class dlgWinRecipeDB(QDialog, Ui_dlgRecipeDB):
    def __init__(self):
        super(dlgWinRecipeDB, self).__init__()
        self.setupUi(self)

        self.gbSuchen.setStyleSheet("QGroupBox { background-color: rgb(255, 255, 255); \
                                                border: 3px solid rgb(255, 0, 0); }")
        self.twRecipes.setHorizontalHeaderLabels(["Id", "Name"])
        self.twRecipes.setColumnWidth(1, 500)
        self.twRecipes.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.twRecipes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.show()

        self.pbSuchen.clicked.connect(self.execute_Suchen)
        self.pbDetail.clicked.connect(self.show_selected_recipe)
        self.twRecipes.doubleClicked.connect(self.show_selected_recipe)

    def execute_Suchen(self):
        print("dlgWinRecipeDB: execute_Suchen Enter")
        query_string = "apiKey=" + RestAPIs_constants.SPOONACULAR_API_KEY
        if self.leIngredient.text() != "":
            query_string = query_string + "&query=" + self.cbCuisine.currentText().strip()
        if self.cbCuisine.currentText() != "":
            query_string = query_string + "&cuisine=" + self.cbCuisine.currentText().strip()
        if self.cbType.currentText() != "":
            query_string = query_string + "&type=" + self.cbType.currentText().strip()
        if int(self.spReadyTime.text()) > 0:
            query_string = query_string + "&maxReadyTime=" + self.spReadyTime.text().strip()

        query_string = "https://api.spoonacular.com/recipes/complexSearch?" + query_string + "&" +"number=5"
        # print("dlgWinRecipeDB: execute_Suchen, query_string= ", query_string)
        self.teQueryString.insertPlainText(query_string)
        self.teQueryString.repaint()
        response = RestAPIs_utilities.get_request(query_string)
        RestAPIs_utilities.jprint(response.text)
        recipes = response.json()
        if response.status_code == 200 and len(recipes) != 0:

            # RestAPIs_utilities.jprint(response.text)
            # print("dlgWinRecipeDB: execute_Suchen, response.text= ", recipes["results"])

            # print("dlgWinRecipeDB: execute_Suchen, recipes[results]= ", recipes["results"])
            # RestAPIs_utilities.jprint_to_file("test_data/recipe_short.json",  recipes["results"])
            self.twRecipes.setRowCount(len(recipes["results"]))

            for i in range(len(recipes["results"])):
                self.twRecipes.setItem(i, 0, QtWidgets.QTableWidgetItem(str(recipes["results"][i]["id"])))
                self.twRecipes.setItem(i, 1, QtWidgets.QTableWidgetItem(recipes["results"][i]["title"]))

        else:
            RestAPIs_utilities.show_info(self, winTitle="Info", winInfo="Keine Daten gefunden")

    def show_selected_recipe(self):
        print("dlgWinRecipeDB: show_selected_recipe Enter")
        row = self.twRecipes.currentRow()
        id = self.twRecipes.item(row, 0).text()
        print("dlgWinRecipeDB: show_selected_recipe currentRow= ", str(row), id)
        dlgWin = dlgWinRecipeDBDetail(id)
        result = dlgWin.exec_()
