from PyQt5 import QtWidgets
import cv2


def load_folder():
    folder_path = QtWidgets.QFileDialog.getExistingDirectory()  # 選取特定資料夾
    return folder_path


def load_imgL():
    imgL_path = QtWidgets.QFileDialog.getOpenFileName()
    return imgL_path


def load_imgR():
    imgR_path = QtWidgets.QFileDialog.getOpenFileName()
    return imgR_path
