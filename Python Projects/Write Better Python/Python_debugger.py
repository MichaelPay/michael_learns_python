# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:42:23 2017

@author: Monic
"""

# python debugger
import pdb; pdb.set_trace()  # The only time it's okay to use ';' in python!!!

my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

del my_list[3]  # [5, 2,1, "abcdefg", 3, False, 4]
del my_list[3]  # [5, 2 ,1, 3, 4]
del my_list[4]  # [5, 2 ,1, 3, 4]
