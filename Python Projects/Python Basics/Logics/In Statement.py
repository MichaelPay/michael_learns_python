# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:16:46 2017

@author: Monic
"""
#sees if "cheese" is in the word "cheeseshop"
print('cheese' in 'cheeseshop')

days_open = ['Monday','Tuesday','Wednesday','Thursday','Friday']
today = 'Tuesday'
if today in days_open:
    print("Come on in")

today = 'Saturday'
if today not in days_open:
    print("Sorry we're closed")