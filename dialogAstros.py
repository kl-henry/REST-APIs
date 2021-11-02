import json
import webbrowser

from PySide2.QtGui import QPixmap, QStandardItemModel
from PySide2.QtWidgets import QDialog, QFileDialog, QTreeWidgetItem

from RestAPIs_utilities import getImageFile
from Test_Treeview_Example import StandardItem
from dialogAstros_ui import Ui_dlgAstros


class dlgWinAstros(QDialog, Ui_dlgAstros):
    def __init__(self, response):
        super(dlgWinAstros, self).__init__()
        self.setupUi(self)
        self.response = response
        self.populateTreeView()

        self.pbSave.clicked.connect(self.save_data)

    def save_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);Image Files (*.png)", options=options)
        if fileName:
            # print(fileName)
            with open(fileName, 'w') as outfile:
                json.dump(self.response, outfile)

    def populateTreeView(self):
        self.tvAstroList.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        craft_item = ""
        old_craft = ""

        for loc_data in self.response["people"]:
            # Craft
            old_craft = craft_item
            craft_item = loc_data["craft"]
            # craft = StandardItem(craft_item, 16, set_bold=True)
            new_craft = False
            if craft_item == old_craft:
                # print(craft_item, old_craft)
                astronaut = StandardItem(loc_data["name"], 14)
                craft.appendRow(astronaut)
                # print(loc_data["name"])
            else:
                new_craft = True
                craft = StandardItem(craft_item, 16, set_bold=True)
                astronaut = StandardItem(loc_data["name"], 14)
                craft.appendRow(astronaut)
            if new_craft:
                rootNode.appendRow(craft)
                new_craft = False

        self.tvAstroList.setModel(treeModel)
        self.tvAstroList.expandAll()
