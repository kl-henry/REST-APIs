from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QTreeView

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

app = QApplication()
tree = QTreeView()


items = []
craft = ""
for data in data["people"]:
    # print(data)
    # print(data["name"], data["craft"])

    if craft != data["craft"]:
        craft = data["craft"]
        item = QTreeWidgetItem([data["craft"]])
        print(craft)
        child = QTreeWidgetItem([data["name"]])
    else:
        child = QTreeWidgetItem([data["name"]])
    item.addChild(child)
    items.append(item)

tree.insertTopLevelItems(0, items)

tree.show()
sys.exit(app.exec_())
