from PySide6.QtCore import QObject
from model.video_thread import VideoThread


class Model(QObject):

    def __init__(self):
        super().__init__()
        self._path_to_file = ''
        self._hsv_pitch = 40, 40, 40, 61, 255, 255
        self._hsv_team1 = 50, 0, 130, 130, 255, 255
        self._hsv_team2 = 0, 0, 0, 38, 255, 255
        self._static_camera = False
        self._path_to_save = None
        self._thread = VideoThread(self)
        self._save_option = False

    @property
    def path_to_file(self):
        return self._path_to_file

    @property
    def hsv_pitch(self):
        return self._hsv_pitch

    @property
    def hsv_team1(self):
        return self._hsv_team1

    @property
    def hsv_team2(self):
        return self._hsv_team2

    @property
    def static_camera(self):
        return self._static_camera

    @property
    def path_to_save(self):
        return self._path_to_save

    @property
    def thread(self):
        return self._thread

    @property
    def save_option(self):
        return self._save_option