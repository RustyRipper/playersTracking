import cv2
import numpy as np
from PySide6.QtCore import *

from model.detector import Detector
from model.drawer import Drawer
from model.trcaker import Tracker


class Main(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    change_pixmap_signal2 = Signal(np.ndarray)

    def __init__(self, path1, hsv_pitch, hsv_team1, hsv_team2, static=True, save=None):
        super().__init__()
        self.path1 = path1
        self.hsv_pitch = hsv_pitch
        self.hsv_team1 = hsv_team1
        self.hsv_team2 = hsv_team2
        self.static = static
        print(self.static)
        self.save = save

    def stop(self):
        self.terminate()

    def run(self):
        out = cv2.VideoWriter()
        if self.save is not None:
            out = cv2.VideoWriter(self.save + '/output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
        cap = cv2.VideoCapture(self.path1)
        ground = cv2.imread(r'data\dst2.png')
        scale = 30
        width = int(ground.shape[1] * scale / 100)
        height = int(ground.shape[0] * scale / 100)

        dim = (width, height)
        ground = cv2.resize(ground, dim, interpolation=cv2.INTER_AREA)

        success, frame = cap.read()

        tracker_bool = True

        if self.static:
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
                players = detector.detect_players(frame, self.hsv_pitch, self.hsv_team1, self.hsv_team2)

                if tracker_bool:
                    success, bboxes = tracker.update_frame(frame)

                    if success:
                        frame = drawer.draw_boxes(frame, bboxes)

                frame = drawer.draw_players(players, frame)

                fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
                cv2.putText(frame, str(int(fps)), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                frame = cv2.resize(frame, dim)
                p = drawer.draw_plane(tracker.plane(), players, ground)

                if self.save is not None:
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


if __name__ == "__main__":
    main = Main()
