import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import tensorflow as tf
from PyQt5 import QtWidgets
from torchvision import models, transforms
from torchsummary import summary
from PIL import Image


my_vgg19 = tf.keras.models.load_model('/home/jacky/Desktop/CVDL2022/Hw1-2/utils/my_vgg19.h5')


def load_img():
    img_path = QtWidgets.QFileDialog.getOpenFileName()[0]
    return img_path


def show_train_img():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    label_table = ("airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck")
    fig, axs = plt.subplots(3, 3)
    # axs[0, 0].imshow(x_train[0])
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


def show_data_augmentation(img_path):
    augments = dict()
    img = Image.open(img_path)

    # random rotate
    rotater = transforms.RandomRotation(degrees=(0, 180))
    augments["random rotate"] = rotater(img)

    # random resize
    resize = transforms.RandomResizedCrop(size=(32, 32))
    augments["random resize"] = resize(img)

    # random horizont
    hflipper = transforms.RandomHorizontalFlip(p=0.5)
    augments["random horizont"] = hflipper(img)

    fig, axs = plt.subplots(1, 3)
    i = 0
    for key in augments:
        axs[i].imshow(augments[key])
        axs[i].title.set_text(key)
        axs[i].axis('off')
        i += 1
    plt.show()


def show_acc_and_loss():
    pass


def inference(img_path):
    global my_vgg19
    label_table = ("airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck")
    img = cv2.imread(img_path)
    img = cv2.resize(img, (32, 32))
    label_idx = np.argmax(my_vgg19.predict(np.array([img])), axis=-1)
    return label_table[label_idx[0]]
