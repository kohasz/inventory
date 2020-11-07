from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_mainwindow
import json, os
fooddict = {}
savecheck = False

class ui_mainmenu(QtWidgets.QMainWindow, Ui_mainwindow):
    def __init__(self, parent=None):
        super(ui_mainmenu, self).__init__(parent)
        self.setupUi(self)
        self.addfood.clicked.connect(self.addfooddict)
        self.editfood.clicked.connect(self.savefooddict)
        self.addrecipe.clicked.connect(self.loadfooddict)

    def loadfooddict(self):
        loadfile = open('fooddict.json')
        fooddict = json.load(loadfile)
        print(fooddict)

    def addfooddict(self):
        global savecheck
        name = self.plainfoodname.toPlainText()
        if name not in fooddict:
            calories = self.plaincalories.toPlainText()
            serving = self.plainserving.toPlainText()
            vita = self.plainvita.toPlainText()
            carbs = self.plaincarbs.toPlainText()
            currentfood = {"calories": calories, "serving": serving, "vitamin A": vita, "carbs": carbs}
            fooddict[name] = currentfood
        else:
            if savecheck:
                calories = self.plaincalories.toPlainText()
                serving = self.plainserving.toPlainText()
                vita = self.plainvita.toPlainText()
                carbs = self.plaincarbs.toPlainText()
                currentfood = {"calories": calories, "serving": serving, "vitamin A": vita, "carbs": carbs}
                fooddict[name] = currentfood
                self.addfood.setText("Add food")
                savecheck = False
                print("save", savecheck)
            else:
                self.addfood.setText("Already in. Overwrite?")
                savecheck = True
                print("save", savecheck)


    def savefooddict(self):
        global savecheck ## its own variable?? savecheckbutton
        if not savecheck:
            with open('fooddict.json', 'w') as foods:
                json.dump(fooddict, foods)
                print(fooddict)
        else:
            self.editfood.setText("OVERWRITE??")
            savecheck = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    supergui = ui_mainmenu()
    supergui.show()
    sys.exit(app.exec_())