from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui

import sys
import _thread
import time


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('img/bg.png')))
        self.centralwidget.setPalette(palette)
        input_img = QtGui.QPixmap('img/input_test.png')
        self.input_img.setPixmap(input_img)
        export_img = QtGui.QPixmap('img/output_test.png')
        self.export_img.setPixmap(export_img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
