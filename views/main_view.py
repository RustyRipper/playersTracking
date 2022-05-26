import cv2
import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *

from model.main import Main
from views.ui_mainwindow import Ui_MainWindow
from model.detect_color import DetectColor


class MainWindow(QMainWindow):
    filename = ''
    file_path_to_save = None

    def __init__(self, model, main_controller):
        super(MainWindow, self).__init__()
        self.thread = None
        self.model = model
        self.main_controller = main_controller

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.main_controller.change_filepath)
        self.ui.pushButton.clicked.connect(self.main_controller.change_filepath_to_save)
        self.ui.checkBox_2.clicked.connect(self.main_controller.change_static_camera)
        self.ui.checkBox.clicked.connect(self.save_option)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_3.clicked.connect(self.main_controller.choose_team1)
        self.ui.pushButton_4.clicked.connect(self.main_controller.choose_team2)
        self.ui.pushButton_5.clicked.connect(self.main_controller.choose_field)

        self.ui.ButtonStart.clicked.connect(self.run)

        self.display_width = 640
        self.display_height = 480
        self.ui.label.resize(self.display_width, self.display_height)
        self.ui.label_2.resize(self.display_width, self.display_height)

    def save_option(self):
        self.main_controller.change_save_option()
        if self.ui.checkBox.isChecked():
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)

    @Slot()
    def run(self):
        print(self.ui.checkBox_2.isChecked())
        self.thread = self.model.thread

        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.change_pixmap_signal2.connect(self.update_image2)

        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @Slot(np.ndarray)
    def update_image(self, image_ground):
        qt_image = self.convert_cv_qt(image_ground)
        self.ui.label.setPixmap(qt_image)

    @Slot(np.ndarray)
    def update_image2(self, image_pitch):
        qt_image2 = self.convert_cv_qt(image_pitch)

        self.ui.label_2.setPixmap(qt_image2)

    def convert_cv_qt(self, cv_image):
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
