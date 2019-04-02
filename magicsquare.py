# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:48:38 2019

@author: Nikki
"""

def magic_square(n):
    
    magicSquare = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    i=n//2
    j=n-1
     
    num=n*n
    count=1
     
    while(count<=num):
         if(i==-1 and j==n):    #condition 4
             j=n-2
             i=0
         else:
             if(j==n):      #Column value exceeding
                 j=0
             if(i<0):
                 i=n-1      #Row is becoming -1
         
         if(magicSquare[i][j]!=0):
             j=j-2
             i=i+1
             continue
         
         else: 
             magicSquare[i][j]=count
             count+=1
             
         i=i-1
         j=j+1     #Condition 1
        
        
        
        
    #Conventional Way
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
        
    print("The Sum of Each Row/Coloumn/Diagonal is :"+str(n*(n**2+1)))      #+ or , anything can be used
magic_square(5)    
    