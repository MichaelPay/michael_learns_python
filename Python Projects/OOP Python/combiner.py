# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:41:50 2017

@author: Monic
"""
# OOP challenge
def combiner(list_object):
    temp_list = []
    number_count = 0
    for x in list_object:
        if isinstance(x, str):
            temp_list.append(x)
        if isinstance(x, int):
            number_count += x
    if number_count != 0:
        temp_list.append(str(number_count))
    return ''.join(temp_list)

print(combiner(['michael','pay',9,'food','dude',8]))