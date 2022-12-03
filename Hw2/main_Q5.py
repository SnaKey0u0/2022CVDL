import sys
from utils import Q5
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from myqt5_Q5 import Ui_MainWindow


img_path = None


def load_img(label):
    global img_path
    img_path = QtWidgets.QFileDialog.getOpenFileName()[0]
    if img_path is not None or img_path is not "":
        pixmap = QPixmap(img_path)
        label.setPixmap(pixmap)


def show_img():
    Q5.show_img()


def show_distribution():
    Q5.show_distribution()


def show_model_structure():
    Q5.show_model_structure()


def show_comparision():
    Q5.show_comparision()


def inference(label):
    global img_path
    prediction = Q5.inference(img_path)
    label.setText(prediction)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_load_img.clicked.connect(lambda: load_img(ui.img))
    ui.btn_show_img.clicked.connect(lambda: show_img())
    ui.btn_show_distribution.clicked.connect(lambda: show_distribution())
    ui.btn_show_model_structure.clicked.connect(lambda: show_model_structure())
    ui.btn_show_comparision.clicked.connect(lambda: show_comparision())
    ui.btn_inference.clicked.connect(lambda: inference(ui.prediction))
    ui.img.setScaledContents(True)
    MainWindow.show()
    sys.exit(app.exec_())
