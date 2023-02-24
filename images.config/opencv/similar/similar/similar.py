import cv2
import numpy as np
from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq
import glob
import os
from tkinter import *

import tkinter.constants, tkinter.filedialog

closestDistance = 99999999
mostSimilarImage = ""

def imageToFeature(filename):
    img = cv2.imread(filename, 0)
    img = cv2.resize(img, (200, 100))
    lbp = local_binary_pattern(img, 8*3, 3, method='uniform')
    x = itemfreq(lbp.ravel())
    feature = x[:, 1]/sum(x[:, 1])
    return feature

def distance(x,y):
	sumSq=0.0
	for i in range(len(x)):
		sumSq+=(x[i]-y[i])**2
	return (sumSq**0.5)

query = input("Enter filename: ")
queryFeature = imageToFeature(query)

for filename in glob.iglob('images/*.pgm'):
    databaseFeature = imageToFeature(filename)
    dist = distance(queryFeature,databaseFeature)
    if dist < closestDistance:
        closestDistance = dist
        mostSimilarImage = filename

# Show result
print(mostSimilarImage)
img = cv2.imread(mostSimilarImage, 1)
query = cv2.imread(query, 1)

cv2.imshow("Most Similar ", img)
cv2.imshow("Query ", query)
cv2.waitKey(0)
