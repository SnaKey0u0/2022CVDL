import sys
from PyQt5 import QtWidgets
from utils import Q1, Q2, Q3, Q4
from myqt5_Q1to4 import Ui_MainWindow

img_path = None
video_path = None
folder_path = None


def load_video(label):
    global video_path
    video_path = QtWidgets.QFileDialog.getOpenFileName()[0]
    if video_path != "":
        label.setText("video loaded")
    else:
        label.setText("No video loaded")


def load_img(label):
    global img_path
    img_path = QtWidgets.QFileDialog.getOpenFileName()[0]
    if img_path != "":
        label.setText("img loaded")
    else:
        label.setText("No img loaded")


def load_folder(label):
    global folder_path
    folder_path = QtWidgets.QFileDialog.getExistingDirectory()  # 選取特定資料夾
    if folder_path != "":
        label.setText("folder loaded")
    else:
        label.setText("No folder loaded")


def background_subtraction():
    pass


def preprocessing():
    pass


def video_tracking():
    pass


def perspective_transform():
    pass


def image_reconstruction():
    pass


def compute_the_reconstruction_error():
    pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_load_video.clicked.connect(lambda: load_video(ui.label_0))
    ui.btn_load_img.clicked.connect(lambda: load_img(ui.label_1))
    ui.btn_load_folder.clicked.connect(lambda: load_folder(ui.label_2))
    ui.btn_1_1.clicked.connect(lambda: background_subtraction())
    ui.btn_2_1.clicked.connect(lambda: preprocessing())
    ui.btn_2_2.clicked.connect(lambda: video_tracking())
    ui.btn_3_1.clicked.connect(lambda: perspective_transform())
    ui.btn_4_1.clicked.connect(lambda: image_reconstruction())
    ui.btn_4_2.clicked.connect(lambda: compute_the_reconstruction_error())
    MainWindow.show()
    sys.exit(app.exec_())
