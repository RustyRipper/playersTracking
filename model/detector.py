import cv2
import numpy as np


class Detector:

    def __init__(self):
        self.players = []
        pass

    def detect_players(self, frame_input, hsv_pitch, hsv_team1, hsv_team2):
        self.players = []
        frame = frame_input.copy()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([hsv_pitch[0], hsv_pitch[1], hsv_pitch[2]])
        upper_green = np.array([hsv_pitch[3], hsv_pitch[4], hsv_pitch[5]])

        lower_blue = np.array([hsv_team1[0], hsv_team1[1], hsv_team1[2]])
        upper_blue = np.array([hsv_team1[3], hsv_team1[4], hsv_team1[5]])

        lower_red = np.array([hsv_team2[0], hsv_team2[1], hsv_team2[2]])
        upper_red = np.array([hsv_team2[3], hsv_team2[4], hsv_team2[5]])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        res_bgr = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
        res_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((13, 13), np.uint8)
        thresh = cv2.threshold(res_gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            x, y, w, h = cv2.boundingRect(c)

            if h >= 1.3 * w:
                if w > 5 and h >= 5:

                    player_img = frame[y:y + h, x:x + w]

                    player_hsv = cv2.cvtColor(player_img, cv2.COLOR_BGR2HSV)

                    mask1 = cv2.inRange(player_hsv, lower_blue, upper_blue)
                    res1 = cv2.bitwise_and(player_img, player_img, mask=mask1)
                    res1 = cv2.cvtColor(res1, cv2.COLOR_HSV2BGR)
                    res1 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)

                    nz_count = cv2.countNonZero(res1)
                    mask2 = cv2.inRange(player_hsv, lower_red, upper_red)
                    res2 = cv2.bitwise_and(player_img, player_img, mask=mask2)
                    res2 = cv2.cvtColor(res2, cv2.COLOR_HSV2BGR)
                    res2 = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)

                    nz_counted = cv2.countNonZero(res2)

                    if nz_count >= 20:
                        color = 'team1'
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                        self.players.append([x, y, w, h, color])
                    else:
                        pass
                    if nz_counted >= 20:
                        color = 'team2'
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        self.players.append([x, y, w, h, color])
                    else:
                        pass
        return self.players
