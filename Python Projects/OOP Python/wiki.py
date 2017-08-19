# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 23:01:46 2017

@author: Monic
"""
# wiki

import datetime

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like? Please use the MM/DD format. Enter 'quit' to quit. ")
    if answer.upper() == 'QUIT':
        break
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print('That\'s not a valid date, please try again. ')