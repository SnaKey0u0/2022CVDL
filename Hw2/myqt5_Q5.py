# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hw2-5.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 191, 311))
        self.groupBox.setObjectName("groupBox")
        self.btn_load_img = QtWidgets.QPushButton(self.groupBox)
        self.btn_load_img.setGeometry(QtCore.QRect(20, 20, 151, 21))
        self.btn_load_img.setObjectName("btn_load_img")
        self.btn_show_img = QtWidgets.QPushButton(self.groupBox)
        self.btn_show_img.setGeometry(QtCore.QRect(20, 70, 151, 23))
        self.btn_show_img.setObjectName("btn_show_img")
        self.btn_show_distribution = QtWidgets.QPushButton(self.groupBox)
        self.btn_show_distribution.setGeometry(QtCore.QRect(20, 120, 151, 23))
        self.btn_show_distribution.setObjectName("btn_show_distribution")
        self.btn_show_model_structure = QtWidgets.QPushButton(self.groupBox)
        self.btn_show_model_structure.setGeometry(QtCore.QRect(20, 170, 151, 23))
        self.btn_show_model_structure.setObjectName("btn_show_model_structure")
        self.btn_show_comparision = QtWidgets.QPushButton(self.groupBox)
        self.btn_show_comparision.setGeometry(QtCore.QRect(20, 220, 151, 23))
        self.btn_show_comparision.setObjectName("btn_show_comparision")
        self.btn_inference = QtWidgets.QPushButton(self.groupBox)
        self.btn_inference.setGeometry(QtCore.QRect(20, 270, 151, 23))
        self.btn_inference.setObjectName("btn_inference")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(260, 30, 281, 261))
        self.img.setFrameShape(QtWidgets.QFrame.Box)
        self.img.setText("")
        self.img.setObjectName("img")
        self.prediction = QtWidgets.QLabel(self.centralwidget)
        self.prediction.setGeometry(QtCore.QRect(350, 300, 111, 16))
        self.prediction.setObjectName("prediction")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "5. ResNet50"))
        self.btn_load_img.setText(_translate("MainWindow", "Load Image"))
        self.btn_show_img.setText(_translate("MainWindow", "1. Show Images"))
        self.btn_show_distribution.setText(_translate("MainWindow", "2. Show Distribution"))
        self.btn_show_model_structure.setText(_translate("MainWindow", "3. Show Model Structure"))
        self.btn_show_comparision.setText(_translate("MainWindow", "4. show Comparision"))
        self.btn_inference.setText(_translate("MainWindow", "5. Inference"))
        self.prediction.setText(_translate("MainWindow", "Prediction: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
