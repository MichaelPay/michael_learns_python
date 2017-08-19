#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:33:21 2017

@author: hamsternation
"""

from thieves import Thief


Michael = Thief(name ='Michael')
print(Michael)
print(Michael.sneaky)
print(Michael.agile)
print(Michael.hide(9))
print(Michael.pickpocket())
print(Michael.evade())