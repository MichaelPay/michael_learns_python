# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:20:20 2017

@author: Monic
"""
def disemvowel(word):
    
    word_list = list(word)
    
    def vowel_remover(source_list,target):
        while True:
            try:
                source_list.remove(target)
            except ValueError:
                break
    
    for x in list('aeiouAEIOU'):
        vowel_remover(word_list, x)
    
    word = str(''.join(word_list))
        
    return word

print(disemvowel(input('what word would you like to disemvowel?')))
