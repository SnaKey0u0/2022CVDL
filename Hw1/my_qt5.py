# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './GUI_hw1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 10, 161, 301))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_corner = QtWidgets.QPushButton(self.groupBox)
        self.btn_corner.setGeometry(QtCore.QRect(20, 30, 121, 25))
        self.btn_corner.setObjectName("btn_corner")
        self.btn_intrinsic = QtWidgets.QPushButton(self.groupBox)
        self.btn_intrinsic.setGeometry(QtCore.QRect(20, 70, 121, 25))
        self.btn_intrinsic.setObjectName("btn_intrinsic")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 141, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_extrinsic = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_extrinsic.setGeometry(QtCore.QRect(10, 70, 121, 25))
        self.btn_extrinsic.setObjectName("btn_extrinsic")
        self.box_num_bmp = QtWidgets.QComboBox(self.groupBox_2)
        self.box_num_bmp.setGeometry(QtCore.QRect(20, 30, 101, 25))
        self.box_num_bmp.setObjectName("box_num_bmp")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.box_num_bmp.addItem("")
        self.btn_distortion = QtWidgets.QPushButton(self.groupBox)
        self.btn_distortion.setGeometry(QtCore.QRect(20, 220, 121, 25))
        self.btn_distortion.setObjectName("btn_distortion")
        self.btn_result1 = QtWidgets.QPushButton(self.groupBox)
        self.btn_result1.setGeometry(QtCore.QRect(20, 260, 121, 25))
        self.btn_result1.setObjectName("btn_result1")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 131, 301))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn_load_folder = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_load_folder.setGeometry(QtCore.QRect(20, 50, 91, 25))
        self.btn_load_folder.setObjectName("btn_load_folder")
        self.btn_loadL = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_loadL.setGeometry(QtCore.QRect(20, 150, 91, 25))
        self.btn_loadL.setObjectName("btn_loadL")
        self.btn_loadR = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_loadR.setGeometry(QtCore.QRect(20, 250, 91, 25))
        self.btn_loadR.setObjectName("btn_loadR")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(320, 10, 181, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.btn_show_board = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_show_board.setGeometry(QtCore.QRect(10, 80, 161, 25))
        self.btn_show_board.setObjectName("btn_show_board")
        self.btn_show_vertical = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_show_vertical.setGeometry(QtCore.QRect(10, 120, 161, 25))
        self.btn_show_vertical.setObjectName("btn_show_vertical")
        self.txt_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_2.setGeometry(QtCore.QRect(20, 40, 141, 25))
        self.txt_2.setObjectName("txt_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(320, 190, 181, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.btn_show_disparity_map = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_show_disparity_map.setGeometry(QtCore.QRect(10, 40, 161, 25))
        self.btn_show_disparity_map.setObjectName("btn_show_disparity_map")
        self.btn_check_disparity_value = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_check_disparity_value.setGeometry(QtCore.QRect(10, 80, 161, 25))
        self.btn_check_disparity_value.setObjectName("btn_check_disparity_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CVDL HW1"))
        self.groupBox.setTitle(_translate("MainWindow", "1. Camera Calibration"))
        self.btn_corner.setText(_translate("MainWindow", "1.1 Find Corners"))
        self.btn_intrinsic.setText(_translate("MainWindow", "1.2 Find Intrinsic"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.btn_extrinsic.setText(_translate("MainWindow", "1.3 Find Extrinsic"))
        self.box_num_bmp.setItemText(0, _translate("MainWindow", "1"))
        self.box_num_bmp.setItemText(1, _translate("MainWindow", "2"))
        self.box_num_bmp.setItemText(2, _translate("MainWindow", "3"))
        self.box_num_bmp.setItemText(3, _translate("MainWindow", "4"))
        self.box_num_bmp.setItemText(4, _translate("MainWindow", "5"))
        self.box_num_bmp.setItemText(5, _translate("MainWindow", "6"))
        self.box_num_bmp.setItemText(6, _translate("MainWindow", "7"))
        self.box_num_bmp.setItemText(7, _translate("MainWindow", "8"))
        self.box_num_bmp.setItemText(8, _translate("MainWindow", "9"))
        self.box_num_bmp.setItemText(9, _translate("MainWindow", "10"))
        self.box_num_bmp.setItemText(10, _translate("MainWindow", "11"))
        self.box_num_bmp.setItemText(11, _translate("MainWindow", "12"))
        self.box_num_bmp.setItemText(12, _translate("MainWindow", "13"))
        self.box_num_bmp.setItemText(13, _translate("MainWindow", "14"))
        self.box_num_bmp.setItemText(14, _translate("MainWindow", "15"))
        self.btn_distortion.setText(_translate("MainWindow", "1.4 Find Distortion"))
        self.btn_result1.setText(_translate("MainWindow", "1.5 Show Result"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Load Image"))
        self.btn_load_folder.setText(_translate("MainWindow", "Load Folder"))
        self.btn_loadL.setText(_translate("MainWindow", "Load Image_L"))
        self.btn_loadR.setText(_translate("MainWindow", "Load Image_R"))
        self.groupBox_5.setTitle(_translate("MainWindow", "2. Argumented Reality"))
        self.btn_show_board.setText(_translate("MainWindow", "2.1 Show words on Board"))
        self.btn_show_vertical.setText(_translate("MainWindow", "2.2 Show words Vertically"))
        self.groupBox_7.setTitle(_translate("MainWindow", "3. Stereo Disparity Map"))
        self.btn_show_disparity_map.setText(_translate("MainWindow", "3.1 Stereo Disparity Map"))
        self.btn_check_disparity_value.setText(_translate("MainWindow", "3.2 Check Disparity Value"))

