from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QFileDialog
from model.detect_color import DetectColor
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import cv2


class MainController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model

    @Slot()
    def change_filepath(self):
        self._model._path_to_file = QFileDialog.getOpenFileName()

    @Slot()
    def change_filepath_to_save(self):
        self._model._path_to_save = QFileDialog.getExistingDirectory()

    @Slot()
    def change_static_camera(self):
        self._model._static_camera = not self._model._static_camera

    @Slot()
    def change_save_option(self):
        self._model._save_option = not self._model._save_option

    @Slot()
    def choose_team1(self):
        if self._model.path_to_file != '':
            self._model._hsv_team1 = DetectColor().run(self._model.path_to_file[0], self._model._hsv_team1)

    @Slot()
    def choose_team2(self):
        if self._model.path_to_file != '':
            self._model._hsv_team2 = DetectColor().run(self._model.path_to_file[0], self._model._hsv_team2)

    @Slot()
    def choose_field(self):
        if self._model.path_to_file != '':
            self._model._hsv_pitch = DetectColor().run(self._model.path_to_file[0], self._model._hsv_pitch, True)

    @staticmethod
    def convert_cv_qt(cv_image, width, height):
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_qt_format.scaled(width, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
