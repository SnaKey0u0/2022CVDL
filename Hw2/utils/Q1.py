import cv2
import numpy as np
from sklearn.mixture import GaussianMixture as GMM


def background_subtraction(video_path="Dataset_CvDl_Hw2/Q1_Image/traffic.mp4"):
    count = 0
    cap = cv2.VideoCapture(video_path)
    gmm_model = GMM(n_components=1, covariance_type='full')
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
            # mask = gmm_model.predict(gray.reshape(-1, 1))
            # for i in range(len(mask)):
            #     mask[i]=255
            # mask = mask.reshape(288,352)

            means = max(gmm_model.means_)[0]

            mask[gray-means > std*5] = 255
            mask[gray-means <= std*5] = 0

            # show frame
            cv2.imshow("mask", mask)
            if cv2.waitKey(1) == ord('q'):
                break

        count += 1
        if count == 25:
            frame0to24 = np.array(frame0to24)
            mean = np.mean(frame0to24, axis=0)
            mean = mean.astype(dtype=np.uint8)
            std = np.std(frame0to24, axis=0)
            std[std < 5] = 5  # if standard deviation is less then 5, set to 5
            gmm_model.fit(mean.reshape(-1, 1))

        # show frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    background_subtraction()
