import cv2
from PyQt5 import QtWidgets


def load_img():
    img_path = QtWidgets.QFileDialog.getOpenFileName()
    return img_path


def show_keypoints(img1_path):
    kpdetector = cv2.xfeatures2d.SIFT_create()
    img1 = cv2.imread(img1_path)
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    kp = kpdetector.detect(img1_gray, None)
    output_img = cv2.drawKeypoints(img1_gray, kp, 0)
    cv2.imshow("keypoints", output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def matched_keypoints(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread(img2_path)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Initiate SIFT detector
    kpdetector = cv2.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = kpdetector.detectAndCompute(img1_gray, None)
    kp2, des2 = kpdetector.detectAndCompute(img2_gray, None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(img1_gray, kp1, img2_gray, kp2, good, None,
                              flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow("mached", img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
