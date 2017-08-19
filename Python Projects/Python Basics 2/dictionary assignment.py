# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 12:57:27 2017

@author: Monic
"""


def num_teachers(dictionary):
    teachers = []
    for x in dictionary.keys():
        teachers.append(str(x))
    counts = teachers.count(1)
    return counts

num_teachers({'michael':'cool','raisa':'good','you':'great'})