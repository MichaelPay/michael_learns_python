.# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:12:22 2017

@author: Monic
"""

my_list = [1]
for x in range(1,99):
    my_list.append(my_list[-1]+1)
    print(my_list)

#remove function
my_list.remove(99)

list('hello')

#join and plit

flavors = ['Chocolate','Strawberry','Mint','Peach']
print(', '.join(flavors))

print('My favorite flavors are: ' + ', '.join(flavors))

print("My favorite flavors are: {}".format(', '.join(flavors)))