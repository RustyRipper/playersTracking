import cv2
import numpy as np

cap = cv2.VideoCapture(r'data\video.avi')
ground = cv2.imread(r'data\dst2.png')
scale = 30
width = int(ground.shape[1] * scale / 100)
height = int(ground.shape[0] * scale / 100)

dim = (width, height)
ground = cv2.resize(ground, dim, interpolation=cv2.INTER_AREA)

trackers = cv2.legacy.MultiTracker_create()
success, frame = cap.read()

players = []
points_plane = []


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        points_plane.append((x, y))
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
        if p[4] == 'team2':
            cv2.circle(copy_temp, pp, 7, (0, 0, 255), -1)
        else:
            cv2.circle(copy_temp, pp, 7, (255, 0, 0), -1)
    return copy_temp


def detect_players(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([40, 40, 40])
    upper_green = np.array([61, 255, 255])
    # blue range
    lower_blue = np.array([50, 0, 130])
    upper_blue = np.array([130, 255, 255])
    # Red range
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([38, 255, 255])
    # white range
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

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)

        if h >= 1.3 * w:
            if w > 10 and h >= 10:

                player_img = frame[y:y + h, x:x + w]

                player_hsv = cv2.cvtColor(player_img, cv2.COLOR_BGR2HSV)

                mask1 = cv2.inRange(player_hsv, lower_blue, upper_blue)
                res1 = cv2.bitwise_and(player_img, player_img, mask=mask1)
                res1 = cv2.cvtColor(res1, cv2.COLOR_HSV2BGR)
                res1 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)

                nz_count = cv2.countNonZero(res1)
                print(nz_count)
                mask2 = cv2.inRange(player_hsv, lower_red, upper_red)
                res2 = cv2.bitwise_and(player_img, player_img, mask=mask2)
                res2 = cv2.cvtColor(res2, cv2.COLOR_HSV2BGR)
                res2 = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)

                nz_counted = cv2.countNonZero(res2)
                print(nz_counted)
                if nz_count >= 10:
                    color = 'team1'
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                    players.append([x, y, w, h, color])
                else:
                    pass
                if nz_counted >= 10:
                    color = 'team2'
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    players.append([x, y, w, h, color])
                else:
                    pass


tracking_points = 4

for i in range(tracking_points):
    cv2.imshow("Frame", frame)
    cv2.imshow("Plane", ground)
    cv2.setMouseCallback('Plane', click_event)

    bbox_i = cv2.selectROI("Frame", frame, False)
    tracker_i = cv2.legacy.TrackerCSRT_create()
    trackers.add(tracker_i, frame, bbox_i)

static = True
tracker_bool = True

if static:
    tracker_bool = False

success, bboxes = trackers.update(frame)

while cap.isOpened():

    success, frame = cap.read()
    timer = cv2.getTickCount()
    players = []

    if tracker_bool:
        success, bboxes = trackers.update(frame)

    detect_players(frame)

    if success:
        for bbox in bboxes:
            draw_box(frame, bbox)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, str(int(fps)), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    frame = cv2.resize(frame, dim)
    p = draw_plane(plane(points_plane, bboxes), players)
    cv2.imshow("Frame", frame)
    cv2.imshow('Plane', p)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
