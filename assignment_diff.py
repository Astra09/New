# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:21:59 2019

@author: Nikki
"""

a=input().split()
b=list(map(int,a))
c=[]
for i in range(0,len(b)):
	if b[i]%3!=0:
		c.append(b[i])
for item in c:
    print(item, end=" ")