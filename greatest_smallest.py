#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:11:11 2020

@author: Vedant
"""

# in this programm we will check which number is the highest
# topics learned variables and conditionals
#%%
a=input('please enter a number : ')
b=input('please enter a number : ')
c=input('please enter a number : ')
d=input('please enter a number : ')

a=int(a)
b=int(b)
c=int(c)
d=int(d)


if a>b:
    #print('A>B')
    if a>c:
        #print('A>C')
        if a>d:
            print(a, 'is the greatest')
        else:
            print(d, 'is the greatest')
    else:
        #print('C>A')
        if c > d:
            print(c, 'is the greatest')
        else:
            print(d, 'is the greatest')
else:
    if b>c:
        #print('B>C')
        if b>d:
            print(b, 'is the greatest')
        else:
            print(d, 'is the greatest')
    else:
        #print('c>b')
        if c>d:
            print(c, 'is the greatest')
        else:
            print(d, 'is the greatest')
#-------------------------------------
if a<b:
    #print('A>B')
    if a<c:
        #print('A>C')
        if a<d:
            print(a, 'is the smallest')
        else:
            print(d, 'is the smallest')
    else:
        #print('C>A')
        if c<d:
            print(c, 'is the smallest')
        else:
            print(d, 'is the smallest')
else:
    if b<c:
        #print('B>C')
        if b<d:
            print(b, 'is the smallest')
        else:
            print(d, 'is the smallest')
    else:
        #print('c>b')
        if c<d:
            print(c, 'is the smallest')
        else:
            print(d, 'is the smallest')
            
            
#--------------------------------------------------

# average
x = a+b+c+d
z = x/4
print(z, 'is the average')