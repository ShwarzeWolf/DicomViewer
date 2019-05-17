import pydicom
import cv2 as cv
import PIL
import matplotlib.pyplot as plt
import numpy as np
import functions
from numpy import matrix
from numpy import linalg
import config


firstFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000008.dcm'
secondFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000010.dcm'

dicomFile1 = pydicom.dcmread(firstFile);
dicomFile2 = pydicom.dcmread(secondFile);

image1 = dicomFile1.pixel_array
image2 = dicomFile2.pixel_array

resultedImage = functions.imposeImages(image1, image2)
plt.imshow(resultedImage)
#plt.waitforbuttonpress()

print("enter command");
command = input()

if (command == "crop"):
    croppedImage1 = functions.cropImage(image1, 160, 120, 300, 230)
    croppedImage2 = functions.cropImage(image2, 160, 120, 300, 230)

    resultedImage = functions.imposeImages(croppedImage1, croppedImage2)

    plt.imshow(resultedImage)
    plt.waitforbuttonpress()
elif (command == "changeOpacity"):
    print("enter first image alpha channel:")
    alphaChannel = input()

    config.alpha = float(alphaChannel)
    config.beta = 1 - config.alpha

    resultedImage = functions.imposeImages(image1, image2)
    plt.imshow(resultedImage)
    plt.waitforbuttonpress()
elif (command == "TPI"):
    print("enter points coordinates:")

    resultedImage = functions.matchThreePoints(image1, image2, 100, 100, 21, 21, 56, 234, 100, 101, 21, 23, 56, 234)

    plt.imshow(resultedImage)
    plt.waitforbuttonpress()

#elif (command == "enterInfo"):
   # print("choose file you want to change. Enter 1 or 2")
    #chosenFile = dicomFile1 if (input() == "1") else dicomFile2

    #print(chosenFile.dir())
    #print("choose parameter you want to change?")
    #chosenTag = input()

    #print("enterValue")
    #value = input()

    #chosenFile.ContentDate = value

    #print(chosenFile.ContentDate)

    #chosenFile.save_as()
else:
    print("unknown command")