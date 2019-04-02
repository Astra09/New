# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:09:32 2019

@author: Nikki
"""
import random
year=random.randint(1993,2018)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
