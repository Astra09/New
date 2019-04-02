# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:22:47 2019

@author: Nikki
"""

#Image Enhancement using CLAHE

import cv2

#Read the Image

img=cv2.imread('2.png')

#Preparation for CLAHE

clahe = cv2.createCLAHE()

#Convert to Grayscale Image

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Applying Enhacement

enh_img = clahe.apply(gray_img)

#Save it to a file

cv2.imwrite('Enhace.png',enh_img)

print("Done Enhancing")
