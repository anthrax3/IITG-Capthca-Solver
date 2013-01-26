#!/usr/bin/python
# Author : Rajat Khanduja
# Date : 15/1/13
# 
# This program is meant to modify the input image so that the noise is removed
# and the image is obtained in a format in which it is possible to differentiate
# between different characters.

import cv
import sys
from contrast import increaseContrast, averageMat
from histogram import createHistogram

image = sys.argv[1]

grayImg = cv.LoadImage(image, cv.CV_LOAD_IMAGE_GRAYSCALE)
mat = cv.GetMat(grayImg)

tmpArr = createHistogram(mat, 255)
minimas = []


image = sys.argv[1]

grayImg = cv.LoadImage(image, cv.CV_LOAD_IMAGE_GRAYSCALE)
mat = cv.GetMat(grayImg)

#t = increaseContrast(averageMat(averageMat(mat)))
t = increaseContrast(averageMat(averageMat(averageMat(mat))))
cv.SaveImage(image + "_avg", t)
eroded = cv.CreateMat(t.rows, t.cols, t.type)
dilated = cv.CreateMat(t.rows, t.cols, t.type)
morphGrad = cv.CreateMat(t.rows, t.cols, t.type)


cv.Erode (t, eroded)
cv.Dilate(t, dilated)

for i in range(dilated.rows):
  for j in range(dilated.cols):
    morphGrad[i,j] = dilated[i,j] - eroded[i,j]

cv.SaveImage(image + "_avg_morphed", morphGrad)

