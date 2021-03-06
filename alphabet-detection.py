from handDetector import HandDetector
from game import Game
import cv2
import math
import numpy as np

handDetector = HandDetector(min_detection_confidence=0.7)
webcamFeed = cv2.VideoCapture(0)

game = Game(0, [], [], "ALLIGATOR")
# print(game.word_to_be_guessed)

letter = ""
prevLetter = ""

while True:
    status, image = webcamFeed.read()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    letter = ""

    if(len(handLandmarks) != 0):
        # Test
        # Letter - A (left)
        if((handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]) &
            (handLandmarks[8][2] > handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] > handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])):
            letter = "A"
        # Letter - A (right)
        elif((handLandmarks[4][3] == "Right" and handLandmarks[4][1] < handLandmarks[3][1]) &
            (handLandmarks[8][2] > handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] > handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])):
            letter = "A"
        
        # Letter - B
        if((handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]) &
            (handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] < handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] < handLandmarks[18][2])):
            letter = "B"
        elif((handLandmarks[4][3] == "Right" and handLandmarks[4][1] < handLandmarks[3][1]) &
            (handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] < handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] < handLandmarks[18][2])):
            letter = "B"

        # Letter - C

        # Letter - D

        # Letter - E

        # Letter - F

        # Letter - G

        # Letter - H

        # Letter - I
        if ((handLandmarks[8][2] > handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] > handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] < handLandmarks[18][2])): # Little finger
            letter = "I"

        # Letter - J

        # Letter - K

        # Letter - L

        if ((handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]) or
            (handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]) &
            (handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] > handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            letter = "L"

        # Letter - M

        # Letter - N

        # Letter - O

        # Letter - P

        # Letter - Q

        # Letter - R

        # Letter - S

        # Letter - T

        # Letter - U
        if ((handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            letter = "U"
        
        # Letter - V
        if ((handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            letter = "V"
        
        # Letter - W
        if (((handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]) or #Right Thumb
                (handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]) #Left Thumb
            ) & # Thumb
            (handLandmarks[8][2] < handLandmarks[6][2]) & # Index finger
            (handLandmarks[12][2] < handLandmarks[10][2]) & # Middle finger
            (handLandmarks[16][2] > handLandmarks[14][2]) & # Ring finger
            (handLandmarks[20][2] > handLandmarks[18][2])): # Little finger
            letter = "W"

        # Letter - X

        # Letter - Y

        # Letter - Z

    cv2.putText(image, letter, (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)

    # Pre GUI - print output

    if prevLetter != letter:
        prevLetter = letter

        print("---------------------------------")
        print("\n")
        game.guess(letter)
        print(game.word_player_guessed)
        print(game.mistakes)
        print("\n")

    cv2.imshow("Volume", image)
    cv2.waitKey(1)