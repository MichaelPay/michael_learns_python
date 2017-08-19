# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:50:31 2017

@author: Monic
"""

import datetime
import random

now = datetime.datetime.now()

two = datetime.datetime.now()

print(now)

print(two.replace(hour=14))

time = random.randint(1, 19999)
print(time)
