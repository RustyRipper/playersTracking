import cv2
import numpy as np
from PySide6.QtCore import *

from model.detector import Detector
from model.drawer import Drawer
from model.trcaker import Tracker


class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    change_pixmap_signal2 = Signal(np.ndarray)
    WIDTH_PRESENT = 640
    HEIGHT_PRESENT = 400
    WIDTH_SAVE = 640
    HEIGHT_SAVE = 640
    FPS_SAVE = 20

    def __init__(self, model):
        super().__init__()
        self._model = model

    def run(self):
        out = cv2.VideoWriter()

        if self._model.path_to_save is not None and self._model.save_option:
            out = cv2.VideoWriter(self._model.path_to_save + '/output.avi', cv2.VideoWriter_fourcc(*'XVID'),
                                  self.FPS_SAVE,
                                  (self.WIDTH_SAVE, self.HEIGHT_SAVE))

        cap = cv2.VideoCapture(self._model.path_to_file[0])
        ground = cv2.imread(r'data\dst2.png')

        dim = (self.WIDTH_PRESENT, self.HEIGHT_PRESENT)
        ground = cv2.resize(ground, dim, interpolation=cv2.INTER_AREA)

        success, frame = cap.read()

        tracker_bool = True

        if self._model.static_camera:
            tracker_bool = False

        detector = Detector()
        drawer = Drawer()
        tracker = Tracker()
        tracker.getTrackingPoints(frame, ground)
        tracker.update_frame(frame)

        while cap.isOpened():

            success, frame = cap.read()
            timer = cv2.getTickCount()
            if success:
                players = detector.detect_players(frame, self._model.hsv_pitch, self._model.hsv_team1,
                                                  self._model.hsv_team2)

                if tracker_bool:
                    success, bboxes = tracker.update_frame(frame)

                    if success:
                        frame = drawer.draw_boxes(frame, bboxes)

                frame = drawer.draw_players(players, frame)

                fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
                cv2.putText(frame, str(int(fps)), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                frame = cv2.resize(frame, dim)
                pitch = drawer.draw_plane(tracker.plane(), players, ground)

                if self._model.path_to_save is not None and self._model.save_option:
                    out.write(cv2.resize(pitch, (self.WIDTH_SAVE, self.HEIGHT_SAVE)))

                self.change_pixmap_signal.emit(pitch)
                self.change_pixmap_signal2.emit(frame)

                if cv2.waitKey(1) & 0XFF == ord('q'):
                    break
            else:
                break

        out.release()
        print("save")
        cap.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.terminate()
