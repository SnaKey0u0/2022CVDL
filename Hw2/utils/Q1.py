import cv2
import numpy as np


def background_subtraction(video_path="Dataset_CvDl_Hw2/Q1_Image/traffic.mp4"):
    count = 0
    cap = cv2.VideoCapture(video_path)
    frame0to24 = list()

    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = np.zeros(gray.shape)
        seg = np.zeros(frame.shape)

        if count <= 24:
            frame0to24.append(gray)
        else:
            diff = cv2.absdiff(gray, mean)  # 處理溢位，不使用subtract
            mask[diff > std*5] = 255
            mask[diff <= std*5] = 0

            mask = mask.astype(np.uint8)  # 轉成整數
            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # 1 => 3 channel
            seg = np.bitwise_and(frame, mask)  # masking

        count += 1
        if count == 25:
            frame0to24 = np.array(frame0to24)
            mean = np.mean(frame0to24, axis=0)
            mean = mean.astype(dtype=np.uint8)  # 轉成整數
            std = np.std(frame0to24, axis=0)
            std[std < 5] = 5  # if standard deviation is less then 5, set to 5

        # show frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

        # show frame
        cv2.imshow("mask", mask)
        if cv2.waitKey(1) == ord('q'):
            break

        # show frame
        cv2.imshow("seg", seg)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    background_subtraction()
