import cv2
import numpy as np

cap = cv2.VideoCapture(r'data\2.mp4')
ground = cv2.imread(r'data\dst.jpg')

trackers = cv2.legacy.MultiTracker_create()
success, frame = cap.read()

players = []
points = []


def click_event(event, x, y):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(x, ' ', y)
        cv2.destroyWindow("Plane")


def draw_box(frame, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)


def plane(points, bboxes):
    pts1 = np.float32([[bboxes[0][0], bboxes[0][1]], [bboxes[1][0], bboxes[1][1]], [bboxes[2][0], bboxes[2][1]],
                       [bboxes[3][0], bboxes[3][1]]])
    pts2 = np.float32([[points[0]], [points[1]], [points[2]], [points[3]]])
    return cv2.getPerspectiveTransform(pts1, pts2)


def draw_plane(matrix, players):
    copy_temp = ground.copy()
    for p in players:
        x = p[0] + int(p[2] / 2)
        y = p[1] + p[3]
        pts3 = np.float32([[x, y]])
        pts3o = cv2.perspectiveTransform(pts3[None, :, :], matrix)
        x1 = int(pts3o[0][0][0])
        y1 = int(pts3o[0][0][1])
        pp = (x1, y1)

        cv2.circle(copy_temp, pp, 15, (0, 0, 255), -1)
    return copy_temp


def detect_players():
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_red = np.array([0, 31, 255])
    upper_red = np.array([176, 255, 255])

    lower_white = np.array([0, 0, 0])
    upper_white = np.array([0, 0, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    res_bgr = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    res_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((13, 13), np.uint8)
    thresh = cv2.threshold(res_gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    prev = 0
    font = cv2.FONT_HERSHEY_SIMPLEX

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)

        # Detect players
        if h >= 1.5 * w:
            if w > 15 and h >= 15:

                player_img = frame[y:y + h, x:x + w]
                player_hsv = cv2.cvtColor(player_img, cv2.COLOR_BGR2HSV)
                # If player has blue jersy
                mask1 = cv2.inRange(player_hsv, lower_blue, upper_blue)
                res1 = cv2.bitwise_and(player_img, player_img, mask=mask1)
                res1 = cv2.cvtColor(res1, cv2.COLOR_HSV2BGR)
                res1 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)

                nz_count = cv2.countNonZero(res1)
                # If player has red jersy
                mask2 = cv2.inRange(player_hsv, lower_red, upper_red)
                res2 = cv2.bitwise_and(player_img, player_img, mask=mask2)
                res2 = cv2.cvtColor(res2, cv2.COLOR_HSV2BGR)
                res2 = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)

                nz_countred = cv2.countNonZero(res2)

                if nz_count >= 20:
                    # Mark blue jersy players as france
                    cv2.putText(frame, 'teamBlue', (x - 2, y - 2), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                    players.append([x, y, w, h])
                else:
                    pass
                if nz_countred >= 20:
                    # Mark red jersy players as belgium
                    cv2.putText(frame, 'teamRed', (x - 2, y - 2), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    players.append([x, y, w, h])
                else:
                    pass

        if 1 <= h <= 30 and 1 <= w <= 30:
            player_img = frame[y:y + h, x:x + w]

            player_hsv = cv2.cvtColor(player_img, cv2.COLOR_BGR2HSV)
            # white ball  detection
            mask1 = cv2.inRange(player_hsv, lower_white, upper_white)
            res1 = cv2.bitwise_and(player_img, player_img, mask=mask1)
            res1 = cv2.cvtColor(res1, cv2.COLOR_HSV2BGR)
            res1 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
            nz_count = cv2.countNonZero(res1)

            if nz_count >= 3:
                # detect football
                cv2.putText(frame, 'football', (x - 2, y - 2), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)


k = 4

for i in range(k):
    cv2.imshow("Frame", frame)
    cv2.imshow("Plane", ground)
    cv2.setMouseCallback('Plane', click_event)

    bbox_i = cv2.selectROI("Frame", frame, False)
    tracker_i = cv2.legacy.TrackerCSRT_create()
    trackers.add(tracker_i, frame, bbox_i)

idx = 0

while cap.isOpened():

    timer = cv2.getTickCount()

    success, frame = cap.read()
    players = []
    success, bboxes = trackers.update(frame)

    detect_players()
    if success:
        for bbox in bboxes:
            draw_box(frame, bbox)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, str(int(fps)), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    p = draw_plane(plane(points, bboxes), players)
    cv2.imshow("Frame", frame)
    cv2.imshow('Plane', p)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
