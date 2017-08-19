# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:50:14 2017

@author: Monic
"""

# assert statement
# the assert statement tries if the assertion is True
# if false, the assertion returns with an 
# AssertionError
# https://www.youtube.com/watch?v=7lmCu8wz8ro [26:00]
assert True

try:
    assert False
    
except AssertionError:
    
    print('false man!')
