import cv2
import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import *

from PySide6.QtWidgets import *

from model.video_thread import VideoThread
from views.ui_mainwindow import Ui_MainWindow
from model.detect_color import DetectColor


class MainWindow(QMainWindow):

    DISPLAY_WIDTH = 640
    DISPLAY_HEIGHT = 400

    def __init__(self, model, main_controller):
        super(MainWindow, self).__init__()
        self._thread = None
        self._model = model
        self._main_controller = main_controller

        self._ui = Ui_MainWindow()

        self._ui.setupUi(self)
        self._ui.pushButton_2.clicked.connect(self._main_controller.change_filepath)
        self._ui.pushButton.clicked.connect(self._main_controller.change_filepath_to_save)
        self._ui.checkBox_2.clicked.connect(self._main_controller.change_static_camera)
        self._ui.checkBox.clicked.connect(self.save_option)
        self._ui.pushButton.setEnabled(False)
        self._ui.pushButton_3.clicked.connect(self._main_controller.choose_team1)
        self._ui.pushButton_4.clicked.connect(self._main_controller.choose_team2)
        self._ui.pushButton_5.clicked.connect(self._main_controller.choose_field)

        self._ui.ButtonStart.clicked.connect(self.run)

        self._ui.label.resize(self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
        self._ui.label_2.resize(self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)

    def save_option(self):
        self._main_controller.change_save_option()
        if self._ui.checkBox.isChecked():
            self._ui.pushButton.setEnabled(True)
        else:
            self._ui.pushButton.setEnabled(False)

    @Slot()
    def run(self):
        self._thread = self._model.thread

        self._thread.change_pixmap_signal.connect(self.update_image)
        self._thread.change_pixmap_signal2.connect(self.update_image2)

        self._thread.start()

    def closeEvent(self, event):
        self._thread.stop()
        event.accept()

    @Slot(np.ndarray)
    def update_image(self, image_ground):
        self._ui.label.setPixmap(
            self._main_controller.convert_cv_qt(image_ground, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

    @Slot(np.ndarray)
    def update_image2(self, image_pitch):
        self._ui.label_2.setPixmap(
            self._main_controller.convert_cv_qt(image_pitch, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
