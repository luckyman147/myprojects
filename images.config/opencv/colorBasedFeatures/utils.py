import cv2
import numpy as np

def colorFeature(img):
    means = cv2.mean(img)
    avgB = int(means[0])
    avgG = int(means[1])
    avgR = int(means[2])
    return [avgB,avgG, avgR]

def divideImage(img, blocks):
    windowsize_r = img.shape[0] / blocks
    windowsize_c = img.shape[1] / blocks

    images = []
    for r in range(0,img.shape[0], windowsize_r):
        for c in range(0,img.shape[0], windowsize_c):
            window = img[r:r+windowsize_r,c:c+windowsize_c]
            images.append(window)

    return images

def describeImage(img, blocks):
    featureVector = []
    images = divideImage(img,blocks)
    for image in images:
        means = colorFeature(image)
        featureVector.append( means[0] )
        featureVector.append( means[1] )
        featureVector.append( means[2] )

    return featureVector

def distance(x,y):
	sumSq=0.0
	for i in range(len(x)):
		sumSq+=(x[i]-y[i])**2
	return (sumSq**0.5)
