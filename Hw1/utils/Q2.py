import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


def show_words_on_board(folder_path, text, magic_txt='./img/Q2_Image/Q2_lib/alphabet_lib_onboard.txt'):
    text = text.upper()
    objp = np.zeros((8*11, 3), np.float32)
    objp[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
    calibration_fnames = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    calibration_fnames = sorted(calibration_fnames, key=lambda x: int(x[:-4]))
    for fname in calibration_fnames:
        objpoints = []
        imgpoints = []
        img = cv2.imread(f'{folder_path}/{fname}')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (11, 8), None)
        if ret == True:
            objpoints.append(objp)
            imgpoints.append(corners)
            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
            for i, (char, bias) in enumerate(
                    zip(text,
                        [[7, 5, 0],
                         [4, 5, 0],
                         [1, 5, 0],
                         [7, 2, 0],
                         [4, 2, 0],
                         [1, 2, 0]]
                        )):
                # print(i, char, bias)

                fs = cv2.FileStorage(magic_txt, cv2.FILE_STORAGE_READ)
                fn = fs.getNode(char)
                axis = np.float32(fn.mat().flatten().reshape((-1, 3)))+bias
                # print(axis[0:2])

                for j in range(0, len(axis), 2):
                    a = axis[j:j+2]
                    imgpts, jac = cv2.projectPoints(a, np.float32(rvecs), np.float32(tvecs), mtx, dist)
                    img = cv2.line(
                        img, tuple(imgpts[0][0].astype(int)),
                        tuple(imgpts[1][0].astype(int)),
                        (0, 0, 255),
                        3)

            img = cv2.resize(img, (500, 500))  # 為了呈現方便，可刪
            cv2.imshow('img', img)
            cv2.waitKey(500)

    cv2.destroyAllWindows()


def show_words_vertically(folder_path, text):
    show_words_on_board(folder_path, text, magic_txt="./img/Q2_Image/Q2_lib/alphabet_lib_vertical.txt")
