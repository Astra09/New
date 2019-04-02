# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:44:54 2019

@author: Nikki
"""

from statistics import mean
from scipy import stats
Estimates=[100,100,104,152,147,158,147,524,545,857,859,874,955,741,1000,1000,236,632,625,632,524,847]
Estimates.sort()
m=stats.trim_mean(Estimates,0.1)
print(m)