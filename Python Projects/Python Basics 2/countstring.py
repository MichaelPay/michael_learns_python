# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 18:51:53 2017

@author: Monic
"""

def countstring(arg):
    set_of_letters = set(arg.lower())
    word_count = []
    for x in set_of_letters:
        word_count.append({x:arg.count(x)})
    for x in range(0,len(word_count)):
        print('There are {} occurences of the letter {}. in your word.'.format(list(word_count[x].values()),list(word_count[x].keys())))    
countstring(input('Which word would you like for me to do a letter count on?'))