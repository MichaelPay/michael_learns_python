# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:10:01 2017

@author: Monic
"""

if 5 > 2:
    print("Yes, 5 is greater than 2")
else:
    print('No')


#if and else
age = 5000
if age > 10000:
    print("Wow, over 10,000 days old!")
else:
    print("Keep going! You'll get there!")


#adding elif
age2 = 22000
if age2 > 20000:
    print("Time to retire!")
elif age > 10000:
    print("Lots of time left!")
else:
    print("Time to get started")

#not statement
if not age > 25000:
    print("Whipersnapper")