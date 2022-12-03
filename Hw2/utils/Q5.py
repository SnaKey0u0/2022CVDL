import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_addons as tfa
from tensorflow.keras.applications.resnet50 import ResNet50
from PyQt5 import QtWidgets


label_table = {0: "Cat", 1: "Dog"}


def show_img(folder_path="Dataset_OpenCvDl_Hw2_Q5/inference_dataset"):
    inference_batch = tf.keras.preprocessing.image_dataset_from_directory(folder_path, image_size=(224, 224))
    fig, axs = plt.subplots(1, 2)
    for batch in inference_batch:
        imgs = np.array(batch[0]).astype(np.uint8)
        labels = np.array(batch[1])
        dog_order = random.randint(0, 4)
        cat_order = random.randint(0, 4)
        dog_count = 0
        cat_count = 0
        # print(dog_order)
        # print(cat_order)
        for idx, img in enumerate(imgs):
            if labels[idx] == 0:
                if dog_count == dog_order:
                    axs[0].imshow(img)
                    axs[0].title.set_text(label_table[labels[idx]])
                    axs[0].axis('off')
                else:
                    dog_count += 1
            elif labels[idx] == 1:
                if cat_count == cat_order:
                    axs[1].imshow(img)
                    axs[1].title.set_text(label_table[labels[idx]])
                    axs[1].axis('off')
                else:
                    cat_count += 1
    plt.show()


def show_distribution():
    distribution = cv2.imread("distribution.png")
    cv2.imshow("distribution", distribution)
    cv2.waitKey(0)


def show_model_structure():
    resnet50 = ResNet50(weights='imagenet')
    dense = tf.keras.layers.Dense(1, activation='sigmoid')(resnet50.output)
    model = tf.keras.models.Model(inputs=resnet50.input, outputs=dense)
    model.summary()


def show_comparision():
    resnet50 = ResNet50(weights='imagenet')
    dense = tf.keras.layers.Dense(1, activation='sigmoid')(resnet50.output)
    model = tf.keras.models.Model(inputs=resnet50.input, outputs=dense)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(8e-5),
        # loss=tfa.losses.SigmoidFocalCrossEntropy(alpha=0.4, gamma=1.0),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    model.summary()


def inference(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    model = tf.keras.models.load_model('resnet50_SigmoidFocalCrossEntropy_10.h5')  # best
    result = model.predict(np.reshape(img, (1, 224, 224, 3)))
    result = result.flatten()
    result[result < 0.5] = 0
    result[result >= 0.5] = 1
    result = result.astype(np.uint8)
    if result[0] == 0:
        return "Prediction: Cat"
    elif result[0] == 1:
        return "Prediction: Dog"


if __name__ == '__main__':
    inference("Dataset_OpenCvDl_Hw2_Q5/inference_dataset/Cat/8046.jpg", 11)
