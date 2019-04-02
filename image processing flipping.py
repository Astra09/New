# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:12:28 2019

@author: Nikki
"""

#Flipping the image
from PIL import Image

#OPening the image
img = Image.open('2.png')

#Transposing
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

#TO save in a human readable format
transposed_img.save('character.png')

print('Done Flipping')