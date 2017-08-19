# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:21:42 2017

@author: Monic
"""

dictionary = {'Michael':22, 'Raisa':24, 'Raevan':38}
while True:
    try:
        name = str(input('Whose age would you like to find out about? '))
        print('{} is {} years old!'.format(name.title(), dictionary[name.title()]))
    except KeyError:
        print("Sorry, but that name isn't in the dictionary!")
