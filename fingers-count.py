from handDetector import HandDetector
import cv2
import math
import numpy as np

handDetector = HandDetector(min_detection_confidence=0.7)
webcamFeed = cv2.VideoCapture(0)

while True:
    status, image = webcamFeed.read()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count=0

    if(len(handLandmarks) != 0):
        #we will get y coordinate of finger-tip and check if it lies above middle landmark of that finger
        #details: https://google.github.io/mediapipe/solutions/hands

        if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:       #Right Thumb
            count = count+1
        elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:       #Left Thumb
            count = count+1
        # Index finger - highest point = 8 & lowest 6
        if handLandmarks[8][2] < handLandmarks[6][2]:
            count = count+1
        # Middle finger - highest point = 12 & lowest 10
        if handLandmarks[12][2] < handLandmarks[10][2]:
            count = count+1
        # Ring finger - highest point = 16 & lowest 14
        if handLandmarks[16][2] < handLandmarks[14][2]:
            count = count+1
        # Little finger - highest point = 20 & lowest 18
        if handLandmarks[20][2] < handLandmarks[18][2]:
            count = count+1

        # Test
        # Letter - V
        if ((handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            count = 100

        # Letter - K
        if ((handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            count = 100

    cv2.putText(image, str(count), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
    cv2.imshow("Volume", image)
    cv2.waitKey(1)