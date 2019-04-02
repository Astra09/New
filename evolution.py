# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:48:21 2019

@author: Nikki
"""

with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am Fine")
myfile.close