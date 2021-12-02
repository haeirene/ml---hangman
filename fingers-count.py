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
        # Test
        # Letter - A

        if((handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]) or
            (handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1])):
            count = 1
        
        # Letter - I
        if ((handLandmarks[8][2] > handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] > handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] < handLandmarks[18][2])): # Little finger
            count = 90
        
        # Letter - V
        if ((handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            count = 220
        
        # Letter - W
        if (((handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]) or #Right Thumb
                (handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]) #Left Thumb
            ) & # Thumb
            (handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            count = 230

    cv2.putText(image, str(count), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
    cv2.imshow("Volume", image)
    cv2.waitKey(1)