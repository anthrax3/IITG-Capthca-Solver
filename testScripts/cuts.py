#!/usr/bin/python

import cv
import sys

def createHistogram(mat, value):
  ''' This function basically creates an array of size of the number of columns
      in mat and gives a count of elements that match a particular value.
  '''
  
  counts = [0] * mat.cols
  for j in range(mat.cols): 
    for i in range(mat.rows):
      if mat[i,j] == value:
        counts[j] += 1

  return counts

image = sys.argv[1]

grayImg = cv.LoadImage(image, cv.CV_LOAD_IMAGE_GRAYSCALE)
mat = cv.GetMat(grayImg)

t = createHistogram(mat, 0)
continuousZeros = 0
#for j in range(mat.cols):
#  if t[j] < 5:
#    continuousZeros += 1
#    if continuousZeros > 3:
#      for i in range(mat.rows):
#        mat[i,j] = 0
#  else:
#    continuousZeros = 0
#for j in range(mat.cols):
#  if j % 10 == 0:
#    for i in range(mat.rows):
#      mat[i,j] = 0

cv.SaveImage(image + "_cuts.png", mat)
