from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QFileDialog
from model.detect_color import DetectColor


class MainController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model

    @Slot()
    def change_filepath(self):
        self._model.path_to_file = QFileDialog.getOpenFileName()

    @Slot()
    def change_filepath_to_save(self):
        self._model.path_to_save = QFileDialog.getExistingDirectory()

    @Slot()
    def change_static_camera(self):
        self._model.static_camera = not self._model.static_camera

    @Slot()
    def change_save_option(self):
        self._model.save_option = not self._model.save_option

    @Slot()
    def choose_team1(self):
        self._model.hsv_team1 = DetectColor().run(self._model.path_to_file[0], self._model.hsv_team1)

    @Slot()
    def choose_team2(self):
        self._model.hsv_team2 = DetectColor().run(self._model.path_to_file[0], self._model.hsv_team2)

    @Slot()
    def choose_field(self):
        self._model.hsv_pitch = DetectColor().run(self._model.path_to_file[0], self._model.hsv_pitch)
