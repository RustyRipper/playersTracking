import cv2
import numpy as np


class DetectColor:
    def __init__(self):
        pass

    def nothing(self):
        pass

    def run(self, path, hsv_default):
        cap2 = cv2.VideoCapture(path)
        success, image1 = cap2.read()
        scale = 30
        width = int(image1.shape[1] * scale / 100)
        height = int(image1.shape[0] * scale / 100)
        dim = (width, height)
        image = cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)

        cv2.namedWindow('image')

        cv2.createTrackbar('HMin', 'image', 0, 179, self.nothing)
        cv2.createTrackbar('SMin', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('VMin', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('HMax', 'image', 0, 179, self.nothing)
        cv2.createTrackbar('SMax', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('VMax', 'image', 0, 255, self.nothing)

        cv2.setTrackbarPos('HMin', 'image', hsv_default[0])
        cv2.setTrackbarPos('SMin', 'image', hsv_default[1])
        cv2.setTrackbarPos('VMin', 'image', hsv_default[2])
        cv2.setTrackbarPos('HMax', 'image', hsv_default[3])
        cv2.setTrackbarPos('SMax', 'image', hsv_default[4])
        cv2.setTrackbarPos('VMax', 'image', hsv_default[5])

        ph_min = ps_min = pv_min = ph_max = ps_max = pv_max = 0

        while 1:
            # Get current positions of all trackbars
            h_min = cv2.getTrackbarPos('HMin', 'image')
            s_min = cv2.getTrackbarPos('SMin', 'image')
            v_min = cv2.getTrackbarPos('VMin', 'image')
            h_max = cv2.getTrackbarPos('HMax', 'image')
            s_max = cv2.getTrackbarPos('SMax', 'image')
            v_max = cv2.getTrackbarPos('VMax', 'image')

            lower = np.array([h_min, s_min, v_min])
            upper = np.array([h_max, s_max, v_max])

            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)
            result = cv2.bitwise_and(image, image, mask=mask)

            if (ph_min != h_min) | (ps_min != s_min) | (pv_min != v_min) | (ph_max != h_max) | (ps_max != s_max) | (
                    pv_max != v_max):
                ph_min = h_min
                ps_min = s_min
                pv_min = v_min
                ph_max = h_max
                ps_max = s_max
                pv_max = v_max

            cv2.imshow('image', result)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        print("(h_min = %d , s_min = %d, v_min = %d), (h_max = %d , s_max = %d, v_max = %d)" % (
            h_min, s_min, v_min, h_max, s_max, v_max))

        cv2.destroyAllWindows()
        return h_min, s_min, v_min, h_max, s_max, v_max
