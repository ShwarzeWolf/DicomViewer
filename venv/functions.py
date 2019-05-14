import cv2 as cv
import numpy as np
from PIL import Image
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
    width1, height1 = image1.shape[:2]
    width2, height2 = image2.shape[:2]

    width = width1 if (width1 > width2) else width2
    height = height1 if (height1 > height2) else height2

    rotationMatrix = cv.getRotationMatrix2D((width / 2, height / 2), 0.0, 1.0)

    fittedImage1 = cv.warpAffine(image1, rotationMatrix, (height, width))
    fittedImage2 = cv.warpAffine(image2, rotationMatrix, (height, width))


    return cv.addWeighted(fittedImage1, config.alpha, fittedImage2, config.beta, config.gamma)
