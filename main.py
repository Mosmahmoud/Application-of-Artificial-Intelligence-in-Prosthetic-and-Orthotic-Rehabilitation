import cv2
from cvzone.PoseModule import PoseDetector
import time
import numpy as np
import matplotlib.pyplot as plt

ANG1 = []
ANG2 = []
X_A = []
i=0
#ASS/P1.mp4
#ASS/P2.mp4
cap = cv2.VideoCapture("ASS/P1L.mp4")

decorator = PoseDetector()
while True:
    success, img =cap.read()
    img = cv2.resize(img, (1288,728))
    #img = cv2.imread("ASS/athlete.jpg")
    img = decorator.findPose(img,False)
    lmlist = decorator.findPosition(img, False)

    if len(lmlist) != 0:
        #Right Arm
        # decorator.findAngle(img, 12, 14, 16)
        #Left Arm
        # decorator.findAngle(img, 11, 13, 15)
        #Right leg
        decorator.findAngle(img, 24, 26, 28)
        #left leg
        decorator.findAngle(img, 23, 25, 27)
        #print(decorator.findAngle(img, 23, 25, 27))


        ANG1.append(decorator.findAngle(img, 23, 25, 27))
        ANG2.append(decorator.findAngle(img, 24, 26, 28))
        X_A.append(i)
        i = i + 1



    cv2.imshow("Image",img)

    plt.plot(X_A, ANG1)



    plt.savefig('ASS/graph.jpg')

    cv2.waitKey(1)



# plt.ylim(170, 200)
# plt.xlim(1, 100)

