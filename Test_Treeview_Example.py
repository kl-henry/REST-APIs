import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeView
from PySide2.QtGui import QFont, QColor, QStandardItemModel, QStandardItem

data = {"number": 14,
        "people":
            [{"name": "Mark Vande Hei", "craft": "ISS"},
             {"name": "Oleg Novitskiy", "craft": "ISS"},
             {"name": "Pyotr Dubrov", "craft": "ISS"},
             {"name": "Thomas Pesquet", "craft": "ISS"},
             {"name": "Megan McArthur", "craft": "ISS"},
             {"name": "Shane Kimbrough", "craft": "ISS"},
             {"name": "Akihiko Hoshide", "craft": "ISS"},
             {"name": "Nie Haisheng", "craft": "Tiangong"},
             {"name": "Liu Boming", "craft": "Tiangong"},
             {"name": "Tang Hongbo", "craft": "Tiangong"},
             {"name": "Chris Sembroski", "craft": "Resilience"},
             {"name": "Hayley Arceneaux", "craft": "Resilience"},
             {"name": "Sian Procto", "craft": "Resilience"},
             {"name": "Jared Isaacman", "craft": "Resilience"}],
        "message": "success"}

data_new = {
    "message": "success",
    "number": 7,
    "people": [
        {
            "craft": "ISS",
            "name": "Mark Vande Hei"
        },
        {
            "craft": "ISS",
            "name": "Oleg Novitskiy"
        },
        {
            "craft": "ISS",
            "name": "Pyotr Dubrov"
        },
        {
            "craft": "ISS",
            "name": "Thomas Pesquet"
        },
        {
            "craft": "ISS",
            "name": "Megan McArthur"
        },
        {
            "craft": "ISS",
            "name": "Shane Kimbrough"
        },
        {
            "craft": "ISS",
            "name": "Akihiko Hoshide"
        }
    ]
}


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class ShowAstrosDemo(QMainWindow):
    def __init__(self, data=None):
        super().__init__()
        self.setWindowTitle('World Country Diagram')
        self.resize(500, 700)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        craft_item = ""
        old_craft = ""

        for loc_data in data["people"]:
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

        treeView.setModel(treeModel)
        treeView.expandAll()

        self.setCentralWidget(treeView)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = ShowAstrosDemo(data_new)
    demo.show()

    sys.exit(app.exec_())
