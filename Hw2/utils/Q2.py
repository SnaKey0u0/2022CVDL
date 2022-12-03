import cv2
import numpy as np

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
# params.filterByColor = True
# params.blobColor = 0
params.minArea = 35
params.maxArea = 90
params.minThreshold = 50  # gray level color
params.maxThreshold = 255
params.minCircularity = 0.8  # 是否像圓
params.maxCircularity = 1.0
params.minInertiaRatio = 0.5  # 正圓、橢圓
params.maxInertiaRatio = 1.0
params.minConvexity = 0.9  # 洞洞，1=沒洞洞
params.maxConvexity = 1.0


# params for ShiTomasi corner detection
feature_params = dict(maxCorners=7,
                      qualityLevel=0.3,
                      minDistance=10,
                      blockSize=5)

# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


def kp_binary_mask(img, kps):  # 二值化kp位置
    mask = np.zeros_like(img)
    for kp in kps:
        x, y = kp.pt
        mask = cv2.circle(mask, (int(x), int(y)), color=(255, 255, 255), radius=3, thickness=-1)
    # cv2.imshow("kp_binary_mask", mask)
    # cv2.waitKey(0)
    return mask


def preprocessing(video_path='Dataset_CvDl_Hw2/Q2_Image/optical_flow.mp4'):
    cap = cv2.VideoCapture(video_path)
    blob_detector = cv2.SimpleBlobDetector_create(params)

    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    # preprocessing
    keypoints = blob_detector.detect(old_gray)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=kp_binary_mask(old_gray, keypoints), **feature_params)

    # show kp
    pre = old_frame
    for i in p0:
        # print(i[0])
        pre = cv2.rectangle(pre, tuple(i[0]-5.0), tuple(i[0]+5.0), color=(0, 0, 255))  # 正方形
        pre = cv2.line(pre, (int(i[0][0]), int(i[0][1]-5.0)), (int(i[0][0]), int(i[0][1]+5.0)), color=(0, 0, 255))  # 直線
        pre = cv2.line(pre, (int(i[0][0]-5.0), int(i[0][1])), (int(i[0][0]+5.0), int(i[0][1])), color=(0, 0, 255))  # 橫線
    cv2.imshow("Circle detect", pre)
    cv2.waitKey(0)
    return


def video_tracking(video_path='Dataset_CvDl_Hw2/Q2_Image/optical_flow.mp4'):  # 前半跟上面一樣
    cap = cv2.VideoCapture(video_path)
    blob_detector = cv2.SimpleBlobDetector_create(params)

    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    # preprocessing
    keypoints = blob_detector.detect(old_gray)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=kp_binary_mask(old_gray, keypoints), **feature_params)

    # Create a mask image for drawing purposes
    mask = np.zeros_like(old_frame)

    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            break

        # gray scale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        # Select good points
        if p1 is not None:
            good_new = p1[st == 1]
            good_old = p0[st == 1]

        # draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 0, 255), 2)
            frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)
        img = cv2.add(frame, mask)

        # show frame
        cv2.imshow('frame', img)
        if cv2.waitKey(1) == ord('q'):
            break

        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # preprocessing()
    video_tracking()
