import cv2
import numpy as np

imgR = None


def click_event(event, x, y, flags, disparity):
    eps = 10**-9
    f = 2826
    c_rl = 123
    B = 178
    if event == cv2.EVENT_LBUTTONDOWN:
        dot = cv2.circle(imgR, (x-disparity[y][x], y), radius=0, color=(0, 0, 255), thickness=15)
        cv2.imshow("Right", dot)


def stereo_disparity_map(imgL_path, imgR_path):
    grayL = cv2.imread(imgL_path, cv2.IMREAD_GRAYSCALE)
    grayR = cv2.imread(imgR_path, cv2.IMREAD_GRAYSCALE)

    # numDisparities: 最大視差值和最小視差值之差，須為16的倍數
    # blockSize: 匹配的塊大小，須為5~255的奇數
    stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
    disparity = stereo.compute(grayL, grayR)
    disparity = np.uint8((disparity-np.min(disparity))/(np.max(disparity)-np.min(disparity))
                         * 255)  # 正規化到0~1，再乘255、轉回0-255的整數

    cv2.namedWindow('Disparity')
    cv2.imshow("Disparity", disparity)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def check_disparity_value(imgL_path, imgR_path):
    global imgR
    imgL = cv2.imread(imgL_path)
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    imgR = cv2.imread(imgR_path)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    imgL = cv2.resize(imgL, (0, 0), fx=0.5, fy=0.5)
    grayL = cv2.resize(grayL, (0, 0), fx=0.5, fy=0.5)
    imgR = cv2.resize(imgR, (0, 0), fx=0.5, fy=0.5)
    grayR = cv2.resize(grayR, (0, 0), fx=0.5, fy=0.5)

    # numDisparities: 最大視差值和最小視差值之差，須為16的倍數
    # blockSize: 匹配的塊大小，須為5~255的奇數
    stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
    disparity = stereo.compute(grayL, grayR)
    disparity = np.uint8((disparity-np.min(disparity))/(np.max(disparity)-np.min(disparity))
                         * 255)  # 正規化到0~1，再乘255、轉回0-255的整數

    cv2.namedWindow('Left')
    cv2.setMouseCallback('Left', click_event, disparity)
    cv2.imshow("Left", imgL)
    cv2.namedWindow('Right')
    cv2.imshow("Right", imgR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
