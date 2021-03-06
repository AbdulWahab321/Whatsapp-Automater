# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python_Projects\PyQt5 Progress Bar\imgtotext.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cv import image_to_ascii_art as convert
from actions import Main 
import os

tr = "*.jpg,*.jpeg,*.png,*.jfif,*.ico,*.JPG,*.JPEG,*.PNG,*.JFIF,*.ICO"

def open_file(self,img_inp):
    filter = "Image Files (*.png)"
    fileName = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget,'Open File',os.getcwd(),filter="All Files (*.*)")

    img_inp.setText(fileName[0])


def back(mw):
    mw.destroy()
    os.system("py mmenu.py")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 0, 781, 101))
        self.Title.setObjectName("Title")
        self.img_path_label = QtWidgets.QLabel(self.centralwidget)
        self.img_path_label.setGeometry(QtCore.QRect(20, 130, 121, 31))
        self.img_path_label.setObjectName("img_path_label")
        self.image_path_input = QtWidgets.QLineEdit(self.centralwidget)
        self.image_path_input.setGeometry(QtCore.QRect(140, 130, 181, 31))
        self.image_path_input.setObjectName("image_path_input")
        self.output_path_label = QtWidgets.QLabel(self.centralwidget)
        self.output_path_label.setGeometry(QtCore.QRect(20, 190, 121, 31))
        self.output_path_label.setObjectName("output_path_label")
        self.output_path_input = QtWidgets.QLineEdit(self.centralwidget)
        self.output_path_input.setGeometry(QtCore.QRect(140, 190, 181, 31))
        self.output_path_input.setObjectName("output_path_input")
        self.output_filename_label = QtWidgets.QLabel(self.centralwidget)
        self.output_filename_label.setGeometry(QtCore.QRect(10, 240, 141, 31))
        self.output_filename_label.setObjectName("output_filename_label")
        self.output_filename_input = QtWidgets.QLineEdit(self.centralwidget)
        self.output_filename_input.setGeometry(QtCore.QRect(150, 240, 181, 31))
        self.output_filename_input.setObjectName("output_filename_input")
        
        self.file_dialog = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:open_file(self,self.image_path_input))
        self.file_dialog.setGeometry(QtCore.QRect(330, 130, 71, 31))
        self.file_dialog.setObjectName("file_dialog")
        
        self.folder_dialog = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.output_path_input.setText(Main.FileDialog(isFolder=True)))
        self.folder_dialog.setGeometry(QtCore.QRect(330, 190, 71, 31))
        self.folder_dialog.setObjectName("folder_dialog")
        
        self.convert_btn = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:convert(self.image_path_input.text(),self.output_path_input.text(),self.output_filename_input.text()))
        self.convert_btn.setGeometry(QtCore.QRect(90, 310, 221, 41))
        self.convert_btn.setObjectName("convert_btn")
        
        self.back = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:back(MainWindow))
        self.back.setGeometry(QtCore.QRect(90, 420, 221, 41))
        self.back.setObjectName("convert_btn")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Image to Text Art Converter</span></p></body></html>"))
        self.img_path_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Image Path:</span></p></body></html>"))
        self.output_path_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Output Path:</span></p></body></html>"))
        self.output_filename_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Ouput Filename:</span></p></body></html>"))
        self.convert_btn.setText(_translate("MainWindow", "Convert"))
        self.file_dialog.setText(_translate("MainWindow", "Browse"))
        self.folder_dialog.setText(_translate("MainWindow", "Browse"))
        self.back.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
