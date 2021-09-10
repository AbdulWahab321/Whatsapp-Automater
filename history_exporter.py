# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python_Projects\VC-GUI\ui\history_exporter_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from components.actions import Main
from components.msgboxpy import *

historyFile = "HST0016.dll"

def back(MainWindow):   
    MainWindow.close()


def export(path,name):
    if os.path.exists(path):
        histories = open(historyFile).read()
        open(os.path.join(path,name+".txt"),"w").write(histories)
    else:
        alrt = alert("Given Path does not exists, Do you want to make Directories along the way if it doesn't exists?",Styles.Buttons.OK_CANCEL|Styles.Icons.ICON_QUESTION,"PTHX2D7")
        if alrt == "yes":
            os.makedirs(path)
            histories = open(historyFile).read()
            open(os.path.join(path,name+".txt"),"w").write(histories)
            alert("Successfully Exported!",Styles.Icons.ICON_ASTERISK)
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFixedWidth(800)
        MainWindow.setFixedHeight(600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 90, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 201, 31))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 130, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 130, 201, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 10, 401, 51))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:export(self.lineEdit.text(),self.lineEdit_2.text()))
        self.pushButton.setGeometry(QtCore.QRect(200, 180, 211, 41))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:back(MainWindow))
        self.back_btn.setGeometry(QtCore.QRect(100, 415, 291, 41))
        self.back_btn.setObjectName("back_btn")
        self.retranslateUi(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Path to export history: </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Name of the exported file: </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Export History Wizard</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Export History"))
        self.back_btn.setText(_translate("MainWindow", "Close"))

if __name__ == "pg.history_exporter":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
elif __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())