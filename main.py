import cv2
import numpy as np
from Detector import Detector
from Drawer import Drawer
from Trcaker import Tracker

cap = cv2.VideoCapture(r'data\5.mp4')
ground = cv2.imread(r'data\dst2.png')
scale = 30
width = int(ground.shape[1] * scale / 100)
height = int(ground.shape[0] * scale / 100)

dim = (width, height)
ground = cv2.resize(ground, dim, interpolation=cv2.INTER_AREA)

success, frame = cap.read()

static = False
tracker_bool = True

if static:
    tracker_bool = False

detector = Detector()
drawer = Drawer()
tracker = Tracker()
tracker.getTrackingPoints(frame, ground)
tracker.update(frame)

while cap.isOpened():

    success, frame = cap.read()
    timer = cv2.getTickCount()

    players = []
    players = detector.detect_players(frame)

    if tracker_bool:
        success, bboxes = tracker.update(frame)
        if success:
            frame = drawer.draw_boxes(frame, bboxes)

    frame = drawer.draw_players(players, frame)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, str(int(fps)), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    frame = cv2.resize(frame, dim)
    p = drawer.draw_plane(tracker.plane(), players, ground)

    cv2.imshow("Frame", frame)
    cv2.imshow('Plane', p)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
