
from PyQt5 import QtWidgets
from my_qt5 import Ui_MainWindow
from utils import Q0, Q1, Q2, Q3
import sys

folder_path = None


def load_folder():
    global folder_path
    folder_path = Q0.load_folder()


def load_imgL(todo):
    Q0.load_imgL(todo)


def load_imgR(todo):
    Q0.load_imgR(todo)

def find_corners():
    if folder_path is not None:
        Q1.find_corners(folder_path)
    else:
        print("You stupid, choose a folder")


def find_intrinsic():
    if folder_path is not None:
        ret, mtx, dist, rvecs, tvecs = Q1.find_intrinsic(folder_path)
        print(mtx)
    else:
        print("You stupid, choose a folder")


def find_extrinsic():
    ith_text = int(ui.box_num_bmp.currentText())
    if folder_path is not None:
        rt = Q1.find_extrinsic(folder_path, ith_text-1)
        print(rt)
    else:
        print("You stupid, choose a folder")


def find_distortion():
    if folder_path is not None:
        dist = Q1.find_distortion(folder_path)
        print(dist)
    else:
        print("You stupid, choose a folder")


def show_result():
    if folder_path is not None:
        Q1.show_result(folder_path)
    else:
        print("You stupid, choose a folder")


def show_words_on_board():
    text = ui.txt_2.text()
    Q2.show_words_on_board(folder_path, text)

def show_words_vertically():
    text = ui.txt_2.text()
    Q2.show_words_on_board(folder_path, text)


def stereo_disparity_map(todo):
    Q3.stereo_disparity_map(todo)


def check_disparity_value(todo):
    Q3.check_disparity_value(todo)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    MainWindow = QtWidgets.QMainWindow()  # 放入基底元件
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  # binding click event
    ui.btn_load_folder.clicked.connect(lambda: load_folder())
    ui.btn_loadL.clicked.connect(lambda: load_imgL("load_imgL"))
    ui.btn_loadR.clicked.connect(lambda: load_imgR('load_imgR'))
    ui.btn_corner.clicked.connect(lambda: find_corners())
    ui.btn_intrinsic.clicked.connect(lambda: find_intrinsic())
    ui.btn_extrinsic.clicked.connect(lambda: find_extrinsic())
    ui.btn_distortion.clicked.connect(lambda: find_distortion())
    ui.btn_result1.clicked.connect(lambda: show_result())
    ui.btn_show_board.clicked.connect(lambda: show_words_on_board())
    ui.btn_show_vertical.clicked.connect(lambda: show_words_vertically())
    ui.btn_show_disparity_map.clicked.connect(lambda: stereo_disparity_map('stereo_disparity_map'))
    ui.btn_check_disparity_value.clicked.connect(lambda: check_disparity_value('check_disparity_value'))
    MainWindow.show()  # 顯示元件
    sys.exit(app.exec_())  # 視窗程式結束
