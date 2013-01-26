#!/usr/bin/python

import sys
import logging

def getCuts(hist):

  '''
  This function finds appropriate segments. Refer to problemFormation for 
  more information on the definitions used in this function.
  '''
  #Find all possible lines along which one can cut.
  cuts = []
  onGoingCut = False
  for i in range (len(hist)):
    if not onGoingCut and hist[i] > 0:
      cuts.append(i)
      onGoingCut = True
    elif onGoingCut and hist[i] == 0:
      cuts.append(i)
      onGoingCut = False
  return cuts

def segments(hist, maxAllowedHistVal):
  cuts = getCuts(hist)

