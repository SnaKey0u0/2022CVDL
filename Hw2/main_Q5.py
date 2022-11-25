from PyQt5 import QtWidgets
from myqt5_Q5 import Ui_MainWindow
from utils import Q5
import sys

def load_img():
    pass

def show_img():
    pass

def show_distribution():
    pass

def show_model_structure():
    pass

def show_comparision():
    pass

def inference():
    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_load_img.clicked.connect(lambda: load_img())
    ui.btn_show_img.clicked.connect(lambda: show_img())
    ui.btn_show_distribution.clicked.connect(lambda: show_distribution())
    ui.btn_show_model_structure.clicked.connect(lambda: show_model_structure())
    ui.btn_show_comparision.clicked.connect(lambda: show_comparision())
    ui.btn_inference.clicked.connect(lambda: inference())
    MainWindow.show()
    sys.exit(app.exec_())