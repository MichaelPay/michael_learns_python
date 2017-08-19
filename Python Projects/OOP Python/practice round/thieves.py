#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:29:41 2017

@author: hamsternation
"""

import random
from attributes import Agile, Sneaky
from characters import Character

class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0,1))