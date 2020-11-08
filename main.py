from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_mainwindow
import json, os, time
inventorydb = {}
itemindex = 1

class ui_mainmenu(QtWidgets.QMainWindow, Ui_mainwindow):
    def __init__(self, parent=None):
        super(ui_mainmenu, self).__init__(parent)
        self.setupUi(self)
        self.additempush.clicked.connect(self.add_new_item_inv)
        self.clearallpush.clicked.connect(self.clearmainscreen)
        self.actionSave.triggered.connect(self.saveinvdb)
        self.actionLoad.triggered.connect(self.startuploaddb)
        self.startuploaddb()

    def add_new_item_inv(self):
        global itemindex
        ## make the dictionary entry
        barcode = self.barcodeplain.toPlainText()
        weight = self.weightplaintext.toPlainText()
        weightunit = self.weightunitcombo.currentText()
        isvegan = self.isvegancheck.checkState()
        expday = self.expdayspin.value()
        expmonth = self.expmonthcombo.currentText()
        expyear = self.expyearspin.value()
        expdate = {"day":expday, "month":expmonth, "year":expyear}
        quantity = self.quantityspinbox.value()
        timeadded = time.time()
        currentitem = {"Barcode":barcode, "Weight": weight, "Unit":weightunit, "Is Vegan?":isvegan, "Exp date":expdate, "Quantity":quantity, "Added at":timeadded}
        print(currentitem)
        itemindex += 1
        inventorydb[itemindex] = currentitem

    def saveinvdb(self):
        with open('invdb.json', 'w') as foods:
            json.dump(inventorydb, foods)
            print(inventorydb)

    def clearmainscreen(self):
        self.barcodeplain.setPlainText("")
        self.weightplaintext.setPlainText("")
        self.weightunitcombo.setCurrentIndex(0)
        self.expdayspin.setValue(1)
        self.expmonthcombo.setCurrentIndex(0)
        self.expyearspin.setValue(2020)
        self.typecombo.setCurrentIndex(0)
        self.prodnameplain.setPlainText("")
        self.quantityspinbox.setValue(1)
        self.isvegancheck.setCheckState(0)
        print("clear")

    def startuploaddb(self):
        global inventorydb, itemindex
        loadfile = open('invdb.json')
        inventorydb = json.load(loadfile)
        print(inventorydb)
        itemindex = len(inventorydb) +1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    supergui = ui_mainmenu()
    supergui.show()
    sys.exit(app.exec_())