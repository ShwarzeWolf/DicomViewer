import cv2 as cv
import numpy as np
import config

def matchThreePoints(image1, image2, x1, y1, x2, y2, x3, y3, xx1, yy1, xx2, yy2, xx3, yy3):

    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3]])
    pts2 = np.float32([[xx1, yy1], [xx2, yy2], [xx3, yy3]])

    rotationMatrix = cv.getAffineTransform(pts1, pts2)

    width, height = image2.shape[:2]
    changedSecondImage = cv.warpAffine(image2, rotationMatrix, (height, width))

    return cv.addWeighted(image1, config.alpha, changedSecondImage, config.beta, config.gamma, changedSecondImage)

def cropImage(image, x1, y1, x2, y2):
    return image[x1:x2, y1:y2];

def imposeImages(image1, image2):
    width1, height1 = cv.getSize(image1)
    width2, height2 = cv.getSize(image2)

    if (width1 > width2):
        width = width1
    else:
        width = width2

