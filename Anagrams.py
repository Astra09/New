# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:37:26 2019

@author: Nikki
"""

str1=input("Enter the First String")
str2=input("Enter the Second String")
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")