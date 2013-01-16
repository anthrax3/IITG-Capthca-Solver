#!/usr/bin/python

import cv
import sys

def increaseContrast(mat):
  t = cv.CreateMat(mat.rows, mat.cols, mat.type)
  for i in range(mat.cols):
    for j in range(mat.rows):
      if mat[j,i] >= 210:
        t[j,i] = 255
      else:
        t[j,i] = 0
  return t

def avg(m, i, j):
  s = m[i,j]
  c = 1

  if i > 0:
    s += m[i - 1, j]
    c += 1

    if j > 0:
      s += m[i - 1, j - 1]
      c += 1
    if j < m.cols - 1:
      s += m[i - 1, j + 1]
      c += 1
  
  if i < m.rows - 1:
    s += m[i + 1, j]
    c += 1

    if j > 0:
      s += m[i + 1, j - 1]
      c += 1
    if j < m.cols - 1:
      s += m[i + 1, j + 1]
      c += 1

  if j > 0:
    s += m[i, j - 1]
    c += 1

  if j < m.cols - 1:
    s += m[i, j + 1]
    c += 1

  return (s * 1.0 / c)

def averageMat(m):
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
