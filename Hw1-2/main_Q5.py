from PyQt5 import QtWidgets
from myqt5_Q5 import Ui_MainWindow
from utils import Q5
import sys

x_train = None 
y_train = None
x_test = None
y_test = None
img_path = None


def load_img():
    global img_path
    img_path = Q5.load_img()


def show_train_img():
    global x_train, y_train, x_test, y_test
    x_train, y_train, x_test, y_test = Q5.show_train_img()


def show_model_structure():
    Q5.show_model_structure()


def show_data_augmentation():
    pass


def show_acc_and_loss():
    pass


def inference():
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    MainWindow = QtWidgets.QMainWindow()  # 放入基底元件
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  # binding click event
    ui.load_img.clicked.connect(lambda: load_img())
    ui.btn5_1.clicked.connect(lambda: show_train_img())
    ui.btn5_2.clicked.connect(lambda: show_model_structure())
    ui.btn5_3.clicked.connect(lambda: show_data_augmentation())
    ui.btn5_4.clicked.connect(lambda: show_acc_and_loss())
    ui.btn5_5.clicked.connect(lambda: inference())

    MainWindow.show()  # 顯示元件
    sys.exit(app.exec_())  # 視窗程式結束
