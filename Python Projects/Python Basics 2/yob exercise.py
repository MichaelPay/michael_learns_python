# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:49:04 2017

@author: Monic
"""

# ask the user for their name and year they're born
# calculate the print the year they'll turn 25, 50, 75, and 100
# if they already past any of these ages, skip them

name = input('Hello! Welcome to the age calculator! What is your name? ')

def quartcentennial(yob):
    yob_list = [25,50,75,100]
    for x in yob_list:
        if 2017 > x+yob:
            pass
        else:
            print('Hey {}! You will be {} years old in {}.'.format(name,x,x+yob))


def yob():
    while True:
        try:
            yob = int(input('Okay, to begin, I\'ll need to know which year you\'re born! '))
            if len(str(yob)) == 4:
                break
            else:
                print('Sorry, but I need a year in YYYY format ')
                continue
        except ValueError:
            print('Sorry, but I need a year in YYYY format ')
    return yob

yob = yob()

quartcentennial(yob)


