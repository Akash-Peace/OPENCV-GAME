import numpy
import cv2
import time

def start():
    obs = 0
    img = numpy.zeros((50, 50, 3), dtype='uint8')
    cv2.rectangle(img, (0, 26), (50, 26), (0, 255, 0), 1)
    cv2.rectangle(img, (0, 27), (50, 27), (0, 255, 0), 1)
    cv2.rectangle(img, (0, 28), (50, 28), (0, 255, 0), 1)
    cv2.rectangle(img, (10, 25), (12, 20), (255, 0, 0), 1)

    while True:
        obs += 1
        if obs < 50:
            cv2.rectangle(img, (50 - obs, 25), (50 - obs, 25), (0, 0, 255), 1)
            time.sleep(0.1)
            if cv2.waitKey(125) == ord('j'):
                cv2.rectangle(img, (50 - (obs - 1), 25), (50 - (obs - 1), 25), (0, 0, 0), 1)
                for i in range(1, 4):
                    obs += 1
                    cv2.rectangle(img, (50 - obs, 25), (50 - obs, 25), (0, 0, 255), 1)
                    cv2.rectangle(img, (10, 25 - (i - 1)), (12, 20 - (i - 1)), (0, 0, 0), 1)
                    cv2.rectangle(img, (10, 25 - i), (12, 20 - i), (255, 0, 0), 1)
                    time.sleep(0.1)
                    cv2.rectangle(img, (50 - (obs - 1), 25), (50 - (obs - 1), 25), (0, 0, 0), 1)
                    cv2.imshow("Jumper - Press j to Jump", img)
                    cv2.waitKey(125)
                for i in range(1, 4):
                    obs += 1
                    cv2.rectangle(img, (50 - obs, 25), (50 - obs, 25), (0, 0, 255), 1)
                    cv2.rectangle(img, (10, 22 + (i - 1)), (12, 17 + (i - 1)), (0, 0, 0), 1)
                    cv2.rectangle(img, (10, 22 + i), (12, 17 + i), (255, 0, 0), 1)
                    if (i == 3) and (((50 - obs) == 9 and (22 + i) == 25) or ((50 - obs) == 10 and (22 + i) == 25) or ((50 - obs) == 11 and (22 + i) == 25)):
                        cv2.rectangle(img, (0, 26), (50, 26), (141, 140, 136), 1)
                        cv2.rectangle(img, (0, 27), (50, 27), (141, 140, 136), 1)
                        cv2.rectangle(img, (0, 28), (50, 28), (141, 140, 136), 1)
                        cv2.rectangle(img, (10, 22 + i), (12, 17 + i), (141, 140, 136), 1)
                        cv2.rectangle(img, (50 - obs, 25), (50 - obs, 25), (141, 140, 136), 1)
                        cv2.imshow("Jumper - Press j to Jump", img)
                        cv2.waitKey(1)
                        time.sleep(2)
                        exit()
                    time.sleep(0.1)
                    cv2.rectangle(img, (50 - (obs - 1), 25), (50 - (obs - 1), 25), (0, 0, 0), 1)
                    cv2.imshow("Jumper - Press j to Jump", img)
                    cv2.waitKey(125)
            else:
                if (50 - obs) == 11:
                    cv2.rectangle(img, (0, 26), (50, 26), (141, 140, 136), 1)
                    cv2.rectangle(img, (0, 27), (50, 27), (141, 140, 136), 1)
                    cv2.rectangle(img, (0, 28), (50, 28), (141, 140, 136), 1)
                    cv2.rectangle(img, (50 - obs, 25), (50 - obs, 25), (141, 140, 136), 1)
                    cv2.rectangle(img, (10, 25), (12, 20), (141, 140, 136), 1)
                    cv2.imshow("Jumper - Press j to Jump", img)
                    cv2.waitKey(1)
                    time.sleep(2)
                    exit()
                cv2.rectangle(img, (50 - (obs - 1), 25), (50 - (obs - 1), 25), (0, 0, 0), 1)
            cv2.imshow('Jumper - Press j to Jump', img)
            cv2.waitKey(125)
        else:
            cv2.rectangle(img, (50 - (obs - 1), 25), (50 - (obs - 1), 25), (0, 0, 0), 1)
            obs = 0


