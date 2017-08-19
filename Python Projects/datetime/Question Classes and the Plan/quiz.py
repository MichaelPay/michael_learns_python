# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 23:14:43 2017

@author: Monic
"""

# quiz
import datetime
import os
import random

from questions import Add
from questions import Multiply

class Quiz:
    solutions = {}
    log = []
    def __init__(self):
        for _ in range(10):
            a,b = random.randint(1,10), random.randint(1,10)
            if random.randint(0,1) == 0:
                self.solutions[Multiply(a,b).text] = Multiply(a,b).answer
            else:
                self.solutions[Add(a,b).text] = Add(a,b).answer
    @staticmethod
    def clear():
        os.system('cls' if os.name =='nt' else 'clear')

    def take_quiz(self):
        self.clear()
        self.log.append(datetime.datetime.now())
        for key, value in self.solutions.items():
            answ = int(input('What is: {} '.format(key)))
            if value == answ:
                self.log.append('Correct')
            else:
                self.log.append('Wrong. Your answered: {}  Correct answer: {}'.format(answ, value))
        self.log.append(datetime.datetime.now())
        self.clear()
        print('''
Here is your summary:

You began the Quiz at {} and you ended this quiz at {}.
The total duration of the quiz was {} Minutes {} Seconds.

Here are your results:
    Question 1: {}
    Question 2: {}
    Question 3: {}
    Question 4: {}
    Question 5: {}
    Quesiton 6: {}
    Question 7: {}
    Question 8: {}
    Quesiton 9: {}
    Quesiton 10: {}
    
You got {} out of 10 questions correct.
        
        '''.format(self.log[0].strftime('%m/%d/%Y %H:%M:%S'), 
                   self.log[11].strftime('%m/%d/%Y %H:%M:%S'), 
                   round((self.log[11]-self.log[0]).seconds/60), 
                   (self.log[11]-self.log[0]).seconds%60,
                   self.log[1],
                   self.log[2],
                   self.log[3],
                   self.log[4],
                   self.log[5],
                   self.log[6],
                   self.log[7],
                   self.log[8],
                   self.log[9],
                   self.log[10],
                   self.log.count('Correct')
                   )
        )
        input('Press any key to continue')
        exit()

quiz = Quiz()
quiz.take_quiz()