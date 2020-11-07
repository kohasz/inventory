from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_mainwindow
import json, os
fooddict = {}

class ui_mainmenu(QtWidgets.QMainWindow, Ui_mainwindow):
    def __init__(self, parent=None):
        super(ui_mainmenu, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    supergui = ui_mainmenu()
    supergui.show()
    sys.exit(app.exec_())