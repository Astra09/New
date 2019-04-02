# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:18:01 2019

@author: Nikki
"""

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                
                
a=[5,1,4,2,8]
bubble(a)
            
for i in a:
    print(i)