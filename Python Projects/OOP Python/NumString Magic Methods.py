# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:53:18 2017

@author: Monic
"""

# numstring.py
# a class that holds a float or int as a string
# but allows us to turn it back into an int whenever we want to
class NumString:
    def __init__(self, value):
        self.value = str(value)
    def __str__(self):
        return self.value
    def __int__(self):
        return int(self.value)
    def __float__(self):
        return float(self.value)
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
    def __radd__(self, other):
        return self + other
    def __iadd__(self, other):
        self.value = self + other
        return self.value
    
five = NumString(5)
print(str(five))
print(int(five))
print(float(five))
