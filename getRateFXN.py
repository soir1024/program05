#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 00:37:25 2022

@author: lisarois
"""

choices = [2,5,8,11,22]

def getRate(choices):
    
    while True:
    
        print('Please select an interest rate:')
        
        letterList = ['A','B','C','D','E','F','G','H']
        index = 0
        while index < len(choices):
            letter = letterList[index]
            print(f' {letter}) {choices[index]:>4}%')
            index = index + 1

        selection = input(f' Enter A-{letter[-1]}: ')
        
        if selection=='A' or selection=='B' or selection =='C' or selection == 'D' or selection == 'E' or selection == 'F' or selection == 'G' or selection == 'H':
            if selection =='A':
                choiceFloat=float(choices[0])
                return choiceFloat
            elif selection =='B':
                return float(choices[1])
            elif selection =='C':
                return float(choices[2])
            elif selection =='D':
                return float(choices[3])
            elif selection == 'E':
                return float(choices[4])
            elif selection =='F':
                return float(choices[5])
            elif selection =='G':
                return float(choices[6])
            
        
            else:
                raise ValueError('Invalid input, please enter the appropriate letter.')
        
#print((getRate(choices)))
            

'''
Issues:
    FORMATTING ISSUE: Need A).. Enter... to align underneath Please...
    
    INPUT ISSUE: if i enter G when G is not possible, i get length error
    
    RETURN ISSUE: I don't need the float value to print to screen after user 
    puts in correct input.
    
    RAISE ERROR: Don't think that I have done this correctly, also its not printing 
    the error message to the screen    
'''

def getPrincipal(limit):
    #prinVal = >0 and <=(limit)
    print(f' Enter the principal (limit {limit}):')
    pincipalInput = input()
    if not isinstance(limit,(int,float):
           raise ValueError()         
                     
print(getPrincipal(650000))
    
