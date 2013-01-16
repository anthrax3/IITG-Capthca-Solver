#!/usr/bin/python

import cv
import sys

def createHistogram(mat, value):
  ''' 
  This function basically creates an array of size of the number of columns
  in mat and gives a count of elements that match a particular value.
  '''
  
  counts = [0] * mat.cols
  for j in range(mat.cols): 
    for i in range(mat.rows):
      if mat[i,j] == value:
        counts[j] += 1

  return counts

ERR_MARGIN = 1

def lesser (x, y, errorMargin):
  '''
  Returns True if x + errorMargin < y
  '''
  return x + errorMargin < y

image = sys.argv[1]

grayImg = cv.LoadImage(image, cv.CV_LOAD_IMAGE_GRAYSCALE)
mat = cv.GetMat(grayImg)

tmpArr = createHistogram(mat, 255)
minimas = []

# Store the indices at which we obtain local minimas
for i in range(1, len(tmpArr)):
  if lesser(tmpArr[i],tmpArr[i - 1], ERR_MARGIN) and lesser(tmpArr[i], tmpArr[i + 1], ERR_MARGIN):
    minimas.append(i)    
    for j in range(mat.rows):
      mat[j,i] = 255


print tmpArr
print minimas
cv.SaveImage(image + "_cuts.png", mat)
