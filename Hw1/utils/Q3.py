import cv2
import numpy as np

imgR = None


def click_event(event, x, y, flags, args):
    [disparity, all, img_width] = args
    try:
        if event == cv2.EVENT_LBUTTONDOWN:
            dot = cv2.circle(all, (x-disparity[y][x]+img_width, y), radius=5, color=(0, 0, 255), thickness=-1)
            cv2.imshow("comb", dot)
    except Exception as e:
        pass


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
    disparity = cv2.resize(disparity, (0, 0), fx=0.5, fy=0.5)  # 為了呈現方便，可刪
    cv2.imshow("Disparity", disparity)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def check_disparity_value(imgL_path, imgR_path):
    global imgR
    imgL = cv2.imread(imgL_path)
    imgR = cv2.imread(imgR_path)

    imgL = cv2.resize(imgL, (0, 0), fx=0.5, fy=0.5)  # 為了呈現方便，可刪
    imgR = cv2.resize(imgR, (0, 0), fx=0.5, fy=0.5)  # 為了呈現方便，可刪

    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    # numDisparities: 最大視差值和最小視差值之差，須為16的倍數
    # blockSize: 匹配的塊大小，須為5~255的奇數
    stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
    disparity = stereo.compute(grayL, grayR)
    disparity = np.uint8((disparity-np.min(disparity))/(np.max(disparity)-np.min(disparity))
                         * 255)  # 正規化到0~1，再乘255、轉回0-255的整數

    comb = np.hstack((imgL, imgR))
    cv2.imshow("comb", comb)
    cv2.setMouseCallback('comb', click_event, [disparity, comb, imgL.shape[1]])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
