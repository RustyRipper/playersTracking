import cv2
import numpy as np
from PySide6.QtCore import *

from model.detector import Detector
from model.drawer import Drawer
from model.trcaker import Tracker


class Main(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    change_pixmap_signal2 = Signal(np.ndarray)

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self):
        out = cv2.VideoWriter()
        if self.model.path_to_save is not None and self.model.save_option:
            out = cv2.VideoWriter(self.model.path_to_save + '/output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

        cap = cv2.VideoCapture(self.model.path_to_file[0])
        ground = cv2.imread(r'data\dst2.png')
        scale = 30
        width = int(ground.shape[1] * scale / 100)
        height = int(ground.shape[0] * scale / 100)

        dim = (width, height)
        ground = cv2.resize(ground, dim, interpolation=cv2.INTER_AREA)

        success, frame = cap.read()

        tracker_bool = True

        if self.model.static_camera :
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
                players = detector.detect_players(frame, self.model.hsv_pitch, self.model.hsv_team1, self.model.hsv_team2)

                if tracker_bool:
                    success, bboxes = tracker.update_frame(frame)

                    if success:
                        frame = drawer.draw_boxes(frame, bboxes)

                frame = drawer.draw_players(players, frame)

                fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
                cv2.putText(frame, str(int(fps)), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                frame = cv2.resize(frame, dim)
                p = drawer.draw_plane(tracker.plane(), players, ground)

                if self.model.path_to_save is not None and self.model.save_option:
                    out.write(cv2.resize(p, (640, 480)))
                self.change_pixmap_signal.emit(p)
                self.change_pixmap_signal2.emit(frame)
                # cv2.imshow("Frame", frame)
                # cv2.imshow('Plane', p)
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
