import cv2
import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *

from model.main import Main
from views.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    filename = ''

    def __init__(self, model, main_controller):
        super(MainWindow, self).__init__()
        self.thread = None
        self.model = model
        self.main_controller = main_controller

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.chooseFilmButton_handler)
        self.ui.ButtonStart.clicked.connect(self.test)

        self.display_width = 640
        self.display_height = 480
        self.ui.label.resize(self.display_width, self.display_height)
        self.ui.label_2.resize(self.display_width, self.display_height)

    @Slot()
    def test(self):
        self.thread = Main(str(self.filename[0]))
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.change_pixmap_signal2.connect(self.update_image2)

        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @Slot()
    def chooseFilmButton_handler(self):
        self.filename = QFileDialog.getOpenFileName()

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
