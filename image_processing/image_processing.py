import cv2
import imutils
import numpy as np


def simple_return(image):
    return image


def crop_image(image):
    return image[0:350, 0:350]


detector = cv2.CascadeClassifier('image_processing/cascades/haarcascade_frontalface_default.xml')


def face_detection(image):
    image = imutils.resize(image, width=300)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceRects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5,
                                          minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

    # loop over the faces and draw a rectangle around each
    mask = np.zeros(image.shape[:2], dtype='uint8')
    for (x, y, w, h) in faceRects:
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    image = cv2.bitwise_and(image, image, mask=mask)

    return image


