import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


def find_corners(folder_path):
    calibration_fnames = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    calibration_fnames = sorted(calibration_fnames, key=lambda x: int(x[:-4]))
    for fname in calibration_fnames:
        img = cv2.imread(f'{folder_path}/{fname}')
        ok, corners = cv2.findChessboardCorners(img, (11, 8), None)
        if ok:
            cv2.drawChessboardCorners(img, (11, 8), corners, ok)
            img = cv2.resize(img, (500,500)) # 為了呈現方便，可刪
            cv2.imshow('img', img)
            cv2.waitKey(500)
    cv2.destroyAllWindows()
    


def find_intrinsic(folder_path):
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((8*11,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    objpoints = [] # 3D point in real world space
    imgpoints = [] # 2D points in image plane

    calibration_fnames = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    calibration_fnames = sorted(calibration_fnames, key=lambda x: int(x[:-4]))
    for fname in calibration_fnames:
        img = cv2.imread(f'{folder_path}/{fname}')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ok, corners = cv2.findChessboardCorners(gray, (11, 8), None)
        # print(fname, ok)
        if ok:
            objpoints.append(objp)
            imgpoints.append(corners)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    return ret, mtx, dist, rvecs, tvecs


def find_extrinsic(folder_path, ith):
    ret, mtx, dist, rvecs, tvecs = find_intrinsic(folder_path)
    r, _ = cv2.Rodrigues(np.array(rvecs[ith]))
    rt = np.concatenate((r, tvecs[ith]), axis=1)
    return rt


def find_distortion(folder_path):
    ret, mtx, dist, rvecs, tvecs = find_intrinsic(folder_path)
    return dist


def show_result(folder_path):
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((8*11,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

    objpoints = [] # 3D point in real world space
    imgpoints = [] # 2D points in image plane

    calibration_fnames = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    calibration_fnames = sorted(calibration_fnames, key=lambda x: int(x[:-4]))
    for fname in calibration_fnames:
        img = cv2.imread(f'{folder_path}/{fname}')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ok, corners = cv2.findChessboardCorners(gray, (11, 8), None)
        # print(fname, ok)
        if ok:
            objpoints.append(objp)
            imgpoints.append(corners)

            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

            h,  w = img.shape[:2]
            newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
            dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

            x, y, w, h = roi
            dst = dst[y:y+h, x:x+w]

            img = cv2.resize(img, (500,500)) # 為了呈現方便，可刪
            cv2.putText(img, "Origin", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            dst = cv2.resize(dst, (500,500)) # 為了呈現方便，可刪
            cv2.putText(dst, "Distortion", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            imstack = np.hstack((img,dst))
            cv2.imshow('compare', imstack)
            cv2.waitKey(500)
    cv2.destroyAllWindows()
    return
