# -*- coding: utf-8 -*-

''' Import statements '''
import sys
import numpy as np

def complexity(rcas):
  
  kp = rcas.sum(axis=0)
  kc = rcas.sum(axis=1)
  kp0 = kp.copy()
  kc0 = kc.copy()

  for i in range(1, 20):
    kc_temp = kc.copy()
    kp_temp = kp.copy()
    kp = rcas.T.dot(kc_temp) / kp0
    if i < 19:
      kc = rcas.dot(kp_temp) / kc0
  
  geo_complexity = (kc - kc.mean()) / kc.std()
  prod_complexity = (kp - kp.mean()) / kp.std()

  return geo_complexity, prod_complexity