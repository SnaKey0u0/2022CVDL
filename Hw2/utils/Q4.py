import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

RE = list()


def image_reconstruction(folder_path='Dataset_CvDl_Hw2/Q4_Image'):
    global RE
    fig, ax = plt.subplots(6, 10, figsize=(15, 12), subplot_kw={'xticks': [], 'yticks': []})

    blues = list()
    greens = list()
    reds = list()
    
    for i, name in enumerate(os.listdir(folder_path)):
        img = cv2.cvtColor(cv2.imread(os.path.join(folder_path, name)), cv2.COLOR_BGR2RGB)

        # Splitting into channels
        blue, green, red = cv2.split(img)

        # normalize to 0~1
        df_blue = blue/255
        df_green = green/255
        df_red = red/255

        # 保留的特徵數
        c = 50
        pca_b = PCA(n_components=c)
        pca_g = PCA(n_components=c)
        pca_r = PCA(n_components=c)

        # 降維
        trans_pca_b = pca_b.fit_transform(df_blue)
        trans_pca_g = pca_g.fit_transform(df_green)
        trans_pca_r = pca_r.fit_transform(df_red)

        # print(trans_pca_b.shape)
        # print(trans_pca_r.shape)
        # print(trans_pca_g.shape)

        # 轉回原維度
        b_arr = pca_b.inverse_transform(trans_pca_b)
        g_arr = pca_g.inverse_transform(trans_pca_g)
        r_arr = pca_r.inverse_transform(trans_pca_r)

        # 拼回三通道
        img_reduced = (cv2.merge((b_arr, g_arr, r_arr)))

        # gray?
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img_reduced = cv2.cvtColor((img_reduced*255).astype(np.uint8), cv2.COLOR_BGR2GRAY)

        # compute reconstruction error
        RE.append(np.sum(np.abs(gray_img-gray_img_reduced)))

        # 畫圖
        j = i // 10
        k = i % 10
        #plt.title("Original Image")
        ax[2*j, k].imshow(img)
        #plt.title("Reduced Image")
        ax[2*j+1, k].imshow(img_reduced)
        ax[2*j, 0].set_ylabel('Original')
        ax[2*j+1, 0].set_ylabel('Reconstructed')

    fig.suptitle('PCA decomposition')
    plt.show()


def compute_the_reconstruction_error():
    global RE
    print(RE)


if __name__ == '__main__':
    image_reconstruction()
