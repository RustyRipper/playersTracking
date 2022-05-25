import cv2
import numpy as np


class DetectColor:
    def __init__(self):
        pass

    def nothing(x):
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

        hMin = sMin = vMin = hMax = sMax = vMax = 0
        phMin = psMin = pvMin = phMax = psMax = pvMax = 0

        while 1:
            # Get current positions of all trackbars
            hMin = cv2.getTrackbarPos('HMin', 'image')
            sMin = cv2.getTrackbarPos('SMin', 'image')
            vMin = cv2.getTrackbarPos('VMin', 'image')
            hMax = cv2.getTrackbarPos('HMax', 'image')
            sMax = cv2.getTrackbarPos('SMax', 'image')
            vMax = cv2.getTrackbarPos('VMax', 'image')

            lower = np.array([hMin, sMin, vMin])
            upper = np.array([hMax, sMax, vMax])

            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)
            result = cv2.bitwise_and(image, image, mask=mask)

            if (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (
                    pvMax != vMax):
                phMin = hMin
                psMin = sMin
                pvMin = vMin
                phMax = hMax
                psMax = sMax
                pvMax = vMax

            cv2.imshow('image', result)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
            hMin, sMin, vMin, hMax, sMax, vMax))

        cv2.destroyAllWindows()
        return hMin, sMin, vMin, hMax, sMax, vMax