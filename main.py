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

croppedImage1 = functions.cropImage(image1, 100, 120, 300, 230)
croppedImage2 = functions.cropImage(image2, 160, 120, 300, 230)


resultedImage = functions.imposeImages(croppedImage1, croppedImage2);
#resultedImage = functions.matchThreePoints(croppedImage1, croppedImage2, 0, 1, 40, 41, 1, 100, 0, 0, 40, 40, 101, 100)

plt.imshow(resultedImage);
plt.waitforbuttonpress();

#rotationMatrix = cv.getRotationMatrix2D((config.width / 2, config.height / 2), config.rotationAngle, config.scale)

#cv.addWeighted(croppedImage1, alpha, croppedImage2, beta, gamma, croppedImage2)

#plt.imshow(croppedImage2);
#plt.waitforbuttonpress();