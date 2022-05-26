from PySide6.QtCore import QObject
from model.main import Main


class Model(QObject):
    def __init__(self):
        super().__init__()
        self.path_to_file = ''
        self.hsv_pitch = 40, 40, 40, 61, 255, 255
        self.hsv_team1 = 50, 0, 130, 130, 255, 255
        self.hsv_team2 = 0, 0, 0, 38, 255, 255
        self.static_camera = False
        print(self.static_camera)
        self.path_to_save = None
        self.thread = Main(self)
        self.save_option = False
