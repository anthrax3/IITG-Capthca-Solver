#!/usr/bin/python
# Author : Rajat Khanduja
# Date : 15/1/13
# 
# This program is meant to modify the input image so that the noise is removed
# and the image is obtained in a format in which it is possible to differentiate
# between different characters.

import cv
import sys

def increaseContrast(mat):
  '''
  Function to increase the contrast of the image represented by the input matrix
  "mat". The matrix is of type cvmat of a grayscale image.
  '''
  t = cv.CreateMat(mat.rows, mat.cols, mat.type)
  for i in range(mat.cols):
    for j in range(mat.rows):
      if mat[j,i] >= 210:
        t[j,i] = 255
      else:
        t[j,i] = 0
  return t


def avg(m, i, j):
  '''
  This function finds the average value that should be stored at a pixel.
  The input is the matrix (cvmat) of a grayscale image and the index at which
  the average is required. 
  '''
  sumNeighbours = m[i,j]
  count = 1

  if i > 0:
    sumNeighbours += m[i - 1, j]
    count += 1

    if j > 0:
      sumNeighbours += m[i - 1, j - 1]
      count += 1
    if j < m.cols - 1:
      sumNeighbours += m[i - 1, j + 1]
      count += 1
  
  if i < m.rows - 1:
    sumNeighbours += m[i + 1, j]
    count += 1

    if j > 0:
      sumNeighbours += m[i + 1, j - 1]
      count += 1
    if j < m.cols - 1:
      sumNeighbours += m[i + 1, j + 1]
      count += 1

  if j > 0:
    sumNeighbours += m[i, j - 1]
    count += 1

  if j < m.cols - 1:
    sumNeighbours += m[i, j + 1]
    count += 1

  return (sumNeighbours * 1.0 / count)

def averageMat(m):
  '''
  Function blurs the image by replacing the value at every pixel by the average
  of the value of the pixel and its neighbours.

  The input matrix should be of type cvmat of a grayscale image.
  '''
  t = cv.CreateMat(m.rows, m.cols, m.type)
  for j in range(m.cols):
    for i in range(m.rows):
      t[i,j] = avg(m, i, j)
  
  return t



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
