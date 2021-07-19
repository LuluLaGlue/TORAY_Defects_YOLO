import cv2
import os

for file in os.listdir('.'):
    if (file.split('.')[1] == "avi"):
        vidcap = cv2.VideoCapture(file)
        success, image = vidcap.read()
        count = 0
        while success:
            # save frame as JPEG file
            cv2.imwrite("./img/{}_frame{}.jpg".format(
                file.split('.')[0], count), image)
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
