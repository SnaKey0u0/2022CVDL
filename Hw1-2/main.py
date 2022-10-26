from PyQt5 import QtWidgets
from my_qt5 import Ui_MainWindow
from utils import Q4, Q5
import sys

img1_path = None
img2_path = None


def load_img1():
    global img1_path
    img1_path = Q4.load_img()[0]


def load_img2():
    global img2_path
    img2_path = Q4.load_img()[0]


def show_keypoints():
    print(img1_path)
    Q4.show_keypoints(img1_path)


def matched_keypoints():
    Q4.matched_keypoints(img1_path, img2_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    MainWindow = QtWidgets.QMainWindow()  # 放入基底元件
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  # binding click event
    ui.load_img1.clicked.connect(lambda: load_img1())
    ui.load_img2.clicked.connect(lambda: load_img2())
    ui.btn4_1.clicked.connect(lambda: show_keypoints())
    ui.btn4_2.clicked.connect(lambda: matched_keypoints())

    MainWindow.show()  # 顯示元件
    sys.exit(app.exec_())  # 視窗程式結束
