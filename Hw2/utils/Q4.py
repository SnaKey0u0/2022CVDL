import os
import cv2
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

RE = list()

def image_reconstruction(folder_path='Dataset_CvDl_Hw2/Q4_Image'):
    global RE
    fig, ax = plt.subplots(6, 10, figsize=(15, 12), subplot_kw={'xticks': [], 'yticks': []})
    for i, name in enumerate(os.listdir(folder_path)):

        img = cv2.cvtColor(cv2.imread(os.path.join(folder_path, name)), cv2.COLOR_BGR2RGB)

        # Splitting into channels
        blue, green, red = cv2.split(img)

        df_blue = blue/255
        df_green = green/255
        df_red = red/255

        pca_b = PCA(n_components=10)
        pca_b.fit(df_blue)
        trans_pca_b = pca_b.transform(df_blue)
        pca_g = PCA(n_components=10)
        pca_g.fit(df_green)
        trans_pca_g = pca_g.transform(df_green)
        pca_r = PCA(n_components=10)
        pca_r.fit(df_red)
        trans_pca_r = pca_r.transform(df_red)

        b_arr = pca_b.inverse_transform(trans_pca_b)
        g_arr = pca_g.inverse_transform(trans_pca_g)
        r_arr = pca_r.inverse_transform(trans_pca_r)

        img_reduced = (cv2.merge((b_arr, g_arr, r_arr)))

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img_reduced = cv2.cvtColor((img_reduced*255).astype(np.uint8), cv2.COLOR_BGR2GRAY)

        RE.append(np.sum(np.abs(gray_img-gray_img_reduced)))

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