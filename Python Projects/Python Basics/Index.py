# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:34:45 2017

@author: Monic
"""

alpha = 'abcde'
alpha_list = list(alpha)

#searching for index number using index
print(alpha.index('cd'))

#using index number to print string
print(alpha[2])

#deletion
del alpha_list[2]
print(alpha_list)

#turning string into a list and then deleting a character in the string and then rejoining it back into a string
alpha = list(alpha)
del alpha[2]
alpha = ''.join(alpha)
print(alpha)