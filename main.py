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

plt.imshow(image2);
plt.waitforbuttonpress();




#image3 = functions.matchThreePoints(image 1, image 2)

#plt.imshow(image3);
#plt.waitforbuttonpress();





#rotationMatrix = cv.getRotationMatrix2D((config.width / 2, config.height / 2), config.rotationAngle, config.scale)


#croppedImage1 = image1[160:300, 120:230];
#croppedImage2 = image2[160:300, 120:230];
#cv.addWeighted(croppedImage1, alpha, croppedImage2, beta, gamma, croppedImage2)

#plt.imshow(croppedImage2);
#plt.waitforbuttonpress();