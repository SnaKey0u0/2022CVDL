import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import tensorflow as tf
from PyQt5 import QtWidgets
from torchvision import models
from torchsummary import summary


def load_img():
    img_path = QtWidgets.QFileDialog.getOpenFileName()
    return img_path


def show_train_img():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    label_table = ("airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck")
    fig, axs = plt.subplots(3, 3)
    axs[0, 0].imshow(x_train[0])
    for i in range(3):
        for j in range(3):
            idx = random.randint(0, len(x_train))
            axs[i, j].imshow(x_train[idx])
            axs[i, j].title.set_text(label_table[y_train[idx][0]])
            axs[i, j].axis('off')
    plt.show()
    return x_train, y_train, x_test, y_test


def show_model_structure():
    # tensorflow
    # model_tf = tf.keras.models.load_model(model) # Demo
    # model_tf = tf.keras.applications.VGG19()
    # model_tf.summary()

    # pytorch
    model_torch = models.vgg19()
    summary(model_torch, (3, 32, 32))
    print(model_torch)


def show_data_augmentation():
    pass


def show_acc_and_loss():
    pass


def inference():
    pass
