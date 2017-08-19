# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:02:27 2017

@author: Monic
"""

import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)
        
    def __int__(self):
        return self.value
      
    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return self + other
class D20(Die):
    def __init__(self):
        super().__init__(sides = 20)