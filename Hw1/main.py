
from PyQt5 import QtWidgets
from my_qt5 import Ui_MainWindow
from utils import Q0, Q1, Q2, Q3
import sys

folder_path = None
imgL_path = None
imgR_path = None


def check_path(path):
    if path is not None: 
        if len(path)>0:
            return True
    return False


def load_folder():
    global folder_path
    folder_path = Q0.load_folder()


def load_imgL():
    global imgL_path
    imgL_path = Q0.load_imgL()


def load_imgR():
    global imgR_path
    imgR_path = Q0.load_imgR()

def find_corners():
    if check_path(folder_path):
        Q1.find_corners(folder_path)
    else:
        print("You stupid, choose a folder")


def find_intrinsic():
    if check_path(folder_path):
        ret, mtx, dist, rvecs, tvecs = Q1.find_intrinsic(folder_path)
        print(mtx)
    else:
        print("You stupid, choose a folder")


def find_extrinsic():
    ith_text = int(ui.box_num_bmp.currentText())
    if check_path(folder_path):
        rt = Q1.find_extrinsic(folder_path, ith_text-1)
        print(rt)
    else:
        print("You stupid, choose a folder")


def find_distortion():
    if check_path(folder_path):
        dist = Q1.find_distortion(folder_path)
        print(dist)
    else:
        print("You stupid, choose a folder")


def show_result():
    if check_path(folder_path):
        Q1.show_result(folder_path)
    else:
        print("You stupid, choose a folder")


def show_words_on_board():
    text = ui.txt_2.text()
    if len(text)>0 and len(text)<=6:
        if check_path(folder_path):
            Q2.show_words_on_board(folder_path, text)
        else:
            print("You stupid, choose a folder")
    else:
        print("You stupid, len of text isn't vaild")



def show_words_vertically():
    text = ui.txt_2.text()
    if len(text)>0 and len(text)<=6:
        if check_path(folder_path):
            Q2.show_words_vertically(folder_path, text)
        else:
            print("You stupid, choose a folder")
    else:
        print("You stupid, len of text isn't vaild")


def stereo_disparity_map():
    if check_path(imgL_path[0]) and check_path(imgR_path[0]):
        print(imgL_path[0], imgR_path[0])
        Q3.stereo_disparity_map(imgL_path[0], imgR_path[0])
    else:
        print("You stupid, choose a picture")


def check_disparity_value():
    if check_path(imgL_path[0]) and check_path(imgR_path[0]):
        Q3.check_disparity_value(imgL_path[0], imgR_path[0])
    else:
        print("You stupid, choose a picture")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    MainWindow = QtWidgets.QMainWindow()  # 放入基底元件
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  # binding click event
    ui.btn_load_folder.clicked.connect(lambda: load_folder())
    ui.btn_loadL.clicked.connect(lambda: load_imgL())
    ui.btn_loadR.clicked.connect(lambda: load_imgR())
    ui.btn_corner.clicked.connect(lambda: find_corners())
    ui.btn_intrinsic.clicked.connect(lambda: find_intrinsic())
    ui.btn_extrinsic.clicked.connect(lambda: find_extrinsic())
    ui.btn_distortion.clicked.connect(lambda: find_distortion())
    ui.btn_result1.clicked.connect(lambda: show_result())
    ui.btn_show_board.clicked.connect(lambda: show_words_on_board())
    ui.btn_show_vertical.clicked.connect(lambda: show_words_vertically())
    ui.btn_show_disparity_map.clicked.connect(lambda: stereo_disparity_map())
    ui.btn_check_disparity_value.clicked.connect(lambda: check_disparity_value())
    MainWindow.show()  # 顯示元件
    sys.exit(app.exec_())  # 視窗程式結束
