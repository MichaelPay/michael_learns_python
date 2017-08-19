# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 23:53:24 2017

@author: Monic
"""
from dice import D6
class Hand(list):
    def __init__(self, rolls=0, dice_val =None, *args, **kwargs):
        if not dice_val:
            raise ValueError('YOU HAVE TO PUT A DICE VAL IN THERE!!')
        super().__init__()
        
        for x in range(rolls):
            self.append(dice_val())
        self.sort()
    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice
        

class Yahtzee(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(rolls = 5, dice_val = D6, *args, **kwargs)
    
    @property
    def ones(self):
        return self._by_value(1)
    
    @property
    def twos(self):
        return self._by_value(2)
    
    @property
    def threes(self):
        return self._by_value(3)
    
    @property
    def fours(self):
        return self._by_value(4)
    
    @property
    def fives(self):
        return self._by_value(5)
    
    @property
    def sixes(self):
        return self._by_value(6)
    
    
    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
                
        }