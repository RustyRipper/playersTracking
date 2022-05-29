import cv2
import numpy as np


class Drawer:
    def __init__(self):
        pass

    @staticmethod
    def draw_plane(matrix, players, ground):
        copy_temp = ground.copy()
        for player in players:
            x = player[0] + int(player[2] / 2)
            y = player[1] + player[3]
            pts3 = np.float32([[x, y]])
            pts3o = cv2.perspectiveTransform(pts3[None, :, :], matrix)
            x1 = int(pts3o[0][0][0])
            y1 = int(pts3o[0][0][1])
            pp = (x1, y1)
            if player[4] == 'team2':
                cv2.circle(copy_temp, pp, 7, (0, 0, 255), -1)
            else:
                cv2.circle(copy_temp, pp, 7, (255, 0, 0), -1)
        return copy_temp

    @staticmethod
    def draw_players(players, frame):
        copy_temp = frame.copy()
        for player in players:
            x = player[0]
            y = player[1]
            w = player[2]
            h = player[3]
            color = player[4]
            if color == 'team2':
                cv2.rectangle(copy_temp, (x, y), (x + w, y + h), (0, 0, 255), 3)
            else:
                cv2.rectangle(copy_temp, (x, y), (x + w, y + h), (255, 0, 0), 3)
        return copy_temp

    def draw_boxes(self, frame, bboxes):
        copy_temp = frame.copy()
        for bbox in bboxes:
            copy_temp = self.draw_box(copy_temp, bbox)
        return copy_temp

    @staticmethod
    def draw_box(frame, bbox):
        copy_temp = frame.copy()
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(copy_temp, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)
        return copy_temp
