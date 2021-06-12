# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
import threading 
from processor import Processor
import threading
import requests
import init
import sys  
import os
import untitled

class ExampleApp(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
   
    def __init__(self):    # Main Processor ui class...
        super().__init__()
        
        self.setupUi(self)

        self.btn_select.clicked.connect(self.select)
        self.btn_check.clicked.connect(self.check)
        self.btn_download.clicked.connect(self.download)


    def select(self):    # Select directory metod...
    
        self.file = QtWidgets.QFileDialog.getExistingDirectory(self, "Select file")
        if self.file != "":
            self.line_save.setText(self.file)
        else:
            pass 


    def check(self):    # Start check video metod...
        self.title = self.line_title.text()
        self.url = self.line_url.text()
        self.path = self.line_save.text()
        self.th = Processor(self.title, self.url, self.path)
        threading.Thread(target = self.th.running).start()
        self.th.length.connect(self.append)


    def download(self):    # Start download video metod...
        self.title = self.line_title.text()
        self.url = self.line_url.text()
        self.path = self.line_save.text()
        self.th = Processor(self.title, self.url, self.path)
        threading.Thread(target = self.th.download).start()
        self.th.receiv.connect(self.progress)

    
    def append(self, title, description, thumbnail):    # Start stream metod...

        if title != "":
            self.line_title.setText(title)
            self.text_desc.setPlainText(description) 
            image = QImage()
            image.loadFromData(requests.get(thumbnail).content)
            self.label_prew.setPixmap(QPixmap(image))
            self.label_prew.show()
        else:
            self.msg()
       

    def progress(self, size):    # Progress bar metod...
        self.progressBar.setValue(size)
    
    def msg(self):    # Message metod...
        dialog = QMessageBox()
        dialog.setText("Проверьте правильность ссылки!")
        dialog.setInformativeText("<i>Скопируйте ссылку на видео из строки браузера...</i>")
        dialog.setWindowTitle("Видео недоступно")
        dialog.setStandardButtons(QMessageBox.Cancel)
        dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        dialog.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()