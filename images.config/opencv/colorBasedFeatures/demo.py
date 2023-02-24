import cv2
import numpy as np
from utils import *

img = cv2.imread("car.jpeg")
featureVector = describeImage(img,2)
print(featureVector)
