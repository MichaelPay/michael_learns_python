#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 17:38:13 2017

@author: hamsternation
"""

import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)

class Thief(Character):
    def __init__(self, name, sneaky = True, *kwarg, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky
        
    def pickpocket(self):
        if self.sneaky:
            return bool(random.randint(0,1))
        else:
            return False
    def hide(self, light_level):
        return self.sneaky and light_level < 10

Michael = Thief('Michael', god_mode = 'enabled', noob_mode = 'disabled')
Michael.sneaky = True
print(Michael.pickpocket())


print(Michael.hide(9))
print(Michael.name)
print(Michael.noob_mode)
print(Michael.god_mode)
print(Michael.userclass)
