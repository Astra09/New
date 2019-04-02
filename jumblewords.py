# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:10:29 2019

@author: Nikki
"""
import random

def choose():
    words=['rainbow','computer','science','programming','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
    
def thank(p1n,p2n,p1,p2):
    print(p1n,'Your score is:',p1)
    print(p2n,'Your score is:',p2)
    print('Thanks For Playing')
    print('Have a Nice Day')

def play():
   p1name=input('Player 1 , Enter your name') 
   p2name=input('Player 2 , Enter your name') 
   pp1=0     #Points
   pp2=0     #Points
   turn=0    #To keep track of turn
   while(1):
       #computers task
       picked_word=choose()     #function choose to pick any word
       #create the question
       qn=jumble(picked_word)
       print(qn)
       #player 1
       if turn%2==0:
           print(p1name,'This is your turn')
           ans=input('What is on my mind?')
           if ans==picked_word:
               pp1=pp1+1
               print('Your Score is ',pp1)
           else:
               print('Better Luck Next Time I thought :',picked_word)
           c=input('Press 1 to continue 0 to quit')
           if c==0:
               thank(p1name,p2name,pp1,pp2)
               break
        #player 2
       else:
           print(p2name,'This is your turn')
           ans=input('What is on my mind?')
           if ans==picked_word:
               pp2=pp2+1
               print('Your Score is ',pp2)
           else:
               print('Better Luck Next Time I thought :',picked_word)
           c=input('Press 1 to continue 0 to quit')
           if c==0:
               thank(p1name,p2name,pp1,pp2)
               break
       turn=turn+1
           
                   
        
           

play()