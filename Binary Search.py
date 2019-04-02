# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:39:02 2019

@author: Nikki
"""

def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("Element is present at:"+str(mid))
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1
            else:
                first_pos=mid+1
                
                
    print("Element Not Found")
    print("Number of Iteration"+str(count))            
    
    
    
a=[]
for i in range(1,101):
    a.append(i)
    
binary_search(a,56)