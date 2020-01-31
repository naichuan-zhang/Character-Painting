from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui

import sys
import _thread
import time
import conversion


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

    def start_conversion(self):
        if hasattr(main, 'input_path'):
            self.gif = QtGui.QMovie('img/loading.gif')
            self.loading.setMovie(self.gif)
            self.gif.start()
            _thread.start_new_thread(lambda: self.is_conversion(main.input_path))
        else:
            print("没有选择指定的图片路径")

    def is_conversion(self, import_path):
        t = str(int(time.time()))
        export_path = 'export_img\\export_img' + t + '.png'
        input_char = self.textEdit.toPlainText()
        pix_distance = self.comboBox.currentText()
        is_over = conversion.image_conversion(import_path, export_path, input_char, pix_distance)
        if not is_over:
            self.loading.clear()
            main.show_export_img(export_path)

    def open_file(self):
        filename = QFileDialog.getOpenFileName(caption='Open File')
        if filename[0] != '':
            self.input_path = filename[0]
            self.show_input_img(self.input_path)

    def show_input_img(self, input_path):
        self.input_img.setPixmap(QtGui.QPixmap(input_path))

    def show_export_img(self, export_path):
        self.export_img.setPixmap(QtGui.QPixmap(export_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    # 添加点击事件
    main.pushButton_input.clicked.connect(main.open_file)
    main.pushButton_conversion.clicked.connect(main.start_conversion)
    sys.exit(app.exec_())
