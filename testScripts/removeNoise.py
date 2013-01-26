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
import cuts
import logging
import time

logging.basicConfig(filename="logFiles/removeNoise.log", level=logging.INFO)


image = sys.argv[1]

t = time.localtime()
timeString = str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec) + " on " + str(t.tm_mday) + "-" + str(t.tm_mon) + "-" + str(t.tm_year)

logging.info ("Started processing : " + image + " at " + timeString)

grayImg = cv.LoadImage(image, cv.CV_LOAD_IMAGE_GRAYSCALE)
mat = cv.GetMat(grayImg)

tmpArr = createHistogram(mat, 255)
logging.debug ("Created histogram : " + str(tmpArr))

t = increaseContrast(averageMat(averageMat(averageMat(averageMat(mat)))))
#cv.SaveImage(image + "_avg", t)
eroded = cv.CreateMat(t.rows, t.cols, t.type)
dilated = cv.CreateMat(t.rows, t.cols, t.type)
morphGrad = cv.CreateMat(t.rows, t.cols, t.type)

cv.Erode (t, eroded)
cv.Dilate(t, dilated)

for i in range(dilated.rows):
  for j in range(dilated.cols):
    morphGrad[i,j] = dilated[i,j] - eroded[i,j]

cv.SaveImage(image + "_avg_morphed", morphGrad)
logging.debug ("Morphed and saved")

hist = createHistogram(morphGrad, 255)
cutCols = cuts.getCuts(hist)

for i in cutCols:
  for j in range(morphGrad.rows):
    morphGrad[j,i] = 255

cv.SaveImage(image + "_avg_morphed_cuts", morphGrad)

t = time.localtime()

timeString = str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec) + " on " + str(t.tm_mday) + "-" + str(t.tm_mon) + "-" + str(t.tm_year)
logging.info("Ended process " + image + " at " + timeString)
