# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:22:49 2017

@author: Monic
"""

def keywordargs(**kwargs):
    print(kwargs)

keywordargs(name = 'michael', food = 'jello')

def unpacker(firstname=None, lastname = None):
    for x in [1,2]:
        if firstname and lastname:
            print("Hi {} {}!".format(firstname, lastname))
        else:
            print('Hi no name!')

unpacker(**{'firstname':'Michael','lastname':'Pay'})

course_minutes = {'Python Basics': 232, 'Django Basics': 237, 'Flask Basics':189, 'Java Basics' : 133}
for course, minutes in course_minutes.items():
    print("{} is {} minutes long.".format(course, minutes))

for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz', start = 1):
    print('{}:{}'.format(index, letter))

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(arg,arg1):
    listing = []
    for i in range(0,len(arg1)):
        temp_tup = arg[i],arg1[i]
        listing.append(temp_tup)
    return listing
