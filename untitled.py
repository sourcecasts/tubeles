# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Root\Desktop\tubeles\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(649, 410)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img\\check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(256, 256))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 640, 381))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.line_url = QtWidgets.QLineEdit(self.tab_3)
        self.line_url.setEnabled(True)
        self.line_url.setGeometry(QtCore.QRect(110, 10, 391, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.line_url.setFont(font)
        self.line_url.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_url.setAcceptDrops(True)
        self.line_url.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_url.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;")
        self.line_url.setText("")
        self.line_url.setMaxLength(100)
        self.line_url.setFrame(True)
        self.line_url.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_url.setCursorPosition(0)
        self.line_url.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_url.setDragEnabled(False)
        self.line_url.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_url.setClearButtonEnabled(False)
        self.line_url.setObjectName("line_url")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_3.setObjectName("label_3")
        self.btn_check = QtWidgets.QPushButton(self.tab_3)
        self.btn_check.setEnabled(True)
        self.btn_check.setGeometry(QtCore.QRect(510, 10, 111, 24))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_check.setFont(font)
        self.btn_check.setStyleSheet("background-color: #065fd4;\n"
"border-radius:4px;\n"
"border-color: #065fd4;\n"
"color: #ffffff;")
        self.btn_check.setIconSize(QtCore.QSize(128, 128))
        self.btn_check.setFlat(False)
        self.btn_check.setObjectName("btn_check")
        self.btn_download = QtWidgets.QPushButton(self.tab_3)
        self.btn_download.setEnabled(True)
        self.btn_download.setGeometry(QtCore.QRect(10, 301, 110, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_download.setFont(font)
        self.btn_download.setStyleSheet("background-color: #ff0000;\n"
"border-radius:4px;\n"
"border-color: #ff0000;\n"
"color: #ffffff;")
        self.btn_download.setIconSize(QtCore.QSize(128, 128))
        self.btn_download.setFlat(False)
        self.btn_download.setObjectName("btn_download")
        self.line_title = QtWidgets.QLineEdit(self.tab_3)
        self.line_title.setEnabled(True)
        self.line_title.setGeometry(QtCore.QRect(20, 60, 591, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.line_title.setFont(font)
        self.line_title.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_title.setAcceptDrops(True)
        self.line_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_title.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;")
        self.line_title.setText("")
        self.line_title.setMaxLength(100)
        self.line_title.setFrame(True)
        self.line_title.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_title.setCursorPosition(0)
        self.line_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_title.setDragEnabled(False)
        self.line_title.setPlaceholderText("")
        self.line_title.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_title.setClearButtonEnabled(False)
        self.line_title.setObjectName("line_title")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 612, 201))
        self.groupBox.setStyleSheet("border-radius:4px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.text_desc = QtWidgets.QTextEdit(self.groupBox)
        self.text_desc.setGeometry(QtCore.QRect(260, 50, 341, 131))
        self.text_desc.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;")
        self.text_desc.setPlaceholderText("")
        self.text_desc.setObjectName("text_desc")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 49, 231, 131))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img\\logo.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_prew = QtWidgets.QLabel(self.groupBox)
        self.label_prew.setGeometry(QtCore.QRect(10, 49, 231, 131))
        self.label_prew.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_prew.setText("")
        self.label_prew.setScaledContents(True)
        self.label_prew.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prew.setWordWrap(False)
        self.label_prew.setObjectName("label_prew")
        self.label.raise_()
        self.text_desc.raise_()
        self.label_prew.raise_()
        self.btn_select = QtWidgets.QPushButton(self.tab_3)
        self.btn_select.setEnabled(True)
        self.btn_select.setGeometry(QtCore.QRect(510, 260, 111, 24))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_select.setFont(font)
        self.btn_select.setStyleSheet("background-color: #065fd4;\n"
"border-radius:4px;\n"
"border-color: #065fd4;\n"
"color: #ffffff;")
        self.btn_select.setIconSize(QtCore.QSize(128, 128))
        self.btn_select.setFlat(False)
        self.btn_select.setObjectName("btn_select")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 261, 91, 21))
        self.label_4.setObjectName("label_4")
        self.line_save = QtWidgets.QLineEdit(self.tab_3)
        self.line_save.setEnabled(True)
        self.line_save.setGeometry(QtCore.QRect(90, 261, 411, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.line_save.setFont(font)
        self.line_save.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_save.setAcceptDrops(True)
        self.line_save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_save.setStyleSheet("border: 1px solid #edeef0;\n"
"padding-left: 4px;\n"
"border-radius: 4px;")
        self.line_save.setText("")
        self.line_save.setMaxLength(100)
        self.line_save.setFrame(True)
        self.line_save.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_save.setCursorPosition(0)
        self.line_save.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_save.setDragEnabled(False)
        self.line_save.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_save.setClearButtonEnabled(False)
        self.line_save.setObjectName("line_save")
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setGeometry(QtCore.QRect(130, 301, 491, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.groupBox.raise_()
        self.line_url.raise_()
        self.label_3.raise_()
        self.btn_check.raise_()
        self.btn_download.raise_()
        self.line_title.raise_()
        self.btn_select.raise_()
        self.label_4.raise_()
        self.line_save.raise_()
        self.progressBar.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 29, 634, 251))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(23)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(197)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 281, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "You Tube Video Downloader 1.0"))
        self.line_url.setPlaceholderText(_translate("MainWindow", " https://www.youtube.com/watch"))
        self.label_3.setText(_translate("MainWindow", "Ссылка на видео"))
        self.btn_check.setText(_translate("MainWindow", "Проверить"))
        self.btn_download.setText(_translate("MainWindow", "Скачать"))
        self.btn_select.setText(_translate("MainWindow", "Выбрать"))
        self.label_4.setText(_translate("MainWindow", "Сохранить в"))
        self.line_save.setPlaceholderText(_translate("MainWindow", " Укажите каталог для сохранения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Скачать"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "21"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "22"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "23"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ссылка"))
        self.label_2.setText(_translate("MainWindow", "История загруженных видео"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Активность"))
