import cv2
import numpy as np


def perspective_transform(img_path, video_path):
    cap = cv2.VideoCapture(video_path)
    pts_dst = [0 for i in range(4)]

    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            break

        # resize
        # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        arucoDict = cv2.aruco.Dictionary_get(0)
        arucoParams = cv2.aruco.DetectorParameters_create()
        corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

        # testing
        # if len(corners) > 0:
        #     print(corners, ids)
        #     print("[INFO] detected {} markers for '{}'".format(len(corners), "123"))
        # cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        last = pts_dst
        pts_dst = [0 for i in range(4)]
        count = 0 
        for c, id in zip(corners, ids):
            count+=1
            try:
                pts_dst[id[0]-1] = c[0][id[0]-1]
            except Exception as e:
                print(e)

        # 若是這個frame找到的點不足4個，用上一個點的位置將就一下
        if count < 4:
            pts_dst = last
        pts_dst = np.array(pts_dst)

        # draw dot on 4 corner
        for i in pts_dst:
            frame = cv2.circle(frame, tuple(i), color=(0, 0, 255), radius=5, thickness=-1)

        # Calculate Homography
        img = cv2.imread(img_path)
        pts_src = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])

        h, status = cv2.findHomography(pts_src, pts_dst)

        # Warp source image to destination based on homography
        warped_image = cv2.warpPerspective(img, h, (frame.shape[1],frame.shape[0]))

        # 疊圖
        frame[warped_image>0]=warped_image[warped_image>0]

        # resize
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # show frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    perspective_transform("Dataset_CvDl_Hw2/Q3_Image/logo.png", "Dataset_CvDl_Hw2/Q3_Image/video.mp4")
