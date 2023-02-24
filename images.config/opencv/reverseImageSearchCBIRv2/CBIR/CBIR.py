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

def distance(x,y):
	sumSq=0.0
	for i in range(len(x)):
		sumSq+=(x[i]-y[i])**2
	return (sumSq**0.5)

def imageToFeature(filename):
    img = cv2.imread(filename, 0)
    img = cv2.resize(img, (200, 100))
    lbp = local_binary_pattern(img, 8*3, 3, method='uniform')
    x = itemfreq(lbp.ravel())
    feature = x[:, 1]/sum(x[:, 1])
    return feature

query = input("Enter filename: ")
queryFeature = imageToFeature(query)

resultList = []

for filename in glob.iglob('images/*.*'):
    databaseFeature = imageToFeature(filename)
    dist = distance(queryFeature,databaseFeature)

    resultList.append( (filename, dist) )

sortedResultList  = sorted(resultList, key=lambda tup: resultList[1])
print(sortedResultList)

# Load first five Results
print( sortedResultList[0][0] )

# Concatenate two images
def imageConcat(file1,file2):
	img1 = cv2.imread(file1, 1)
	img1 = cv2.resize(img1, (320, 200))
	img2 = cv2.imread(file2, 1)
	img2 = cv2.resize(img2, (320, 200))
	both = np.hstack((img1,img2))
	return both

# Create Grid
A = imageConcat(sortedResultList[0][0], sortedResultList[1][0])
B = imageConcat(sortedResultList[2][0], sortedResultList[3][0])
both = np.hstack((A,B))
C = imageConcat(sortedResultList[4][0], sortedResultList[5][0])
D = imageConcat(sortedResultList[6][0], sortedResultList[7][0])
both2 = np.hstack((C,D))
both = np.vstack((both,both2))

# Show Image
cv2.imshow("Results", both)
cv2.waitKey(0)
