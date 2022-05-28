import cv2
import numpy as np


class Tracker:

    TRACKING_POINTS = 4

    def __init__(self):
        self.points_plane = []

        self.trackers = cv2.legacy.MultiTracker_create()
        self.bboxes = []

    def plane(self):
        pts1 = np.float32([[self.bboxes[0][0], self.bboxes[0][1]],
                           [self.bboxes[1][0], self.bboxes[1][1]],
                           [self.bboxes[2][0], self.bboxes[2][1]],
                           [self.bboxes[3][0], self.bboxes[3][1]]])
        pts2 = np.float32(
            [[self.points_plane[0]], [self.points_plane[1]], [self.points_plane[2]], [self.points_plane[3]]])
        return cv2.getPerspectiveTransform(pts1, pts2)

    def getTrackingPoints(self, frame, ground):
        for i in range(self.TRACKING_POINTS):
            cv2.imshow("Frame", frame)
            cv2.imshow("Plane", ground)
            cv2.setMouseCallback('Plane', self.click_event)

            bbox_i = cv2.selectROI("Frame", frame, False)
            tracker_i = cv2.legacy.TrackerMIL_create()
            self.trackers.add(tracker_i, frame, bbox_i)

            cv2.destroyWindow("Frame")

    def click_event(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.points_plane.append((x, y))
            print(x, ' ', y)
            cv2.destroyWindow("Plane")

    def update_frame(self, frame):
        success, self.bboxes = self.trackers.update(frame)
        return success, self.bboxes
