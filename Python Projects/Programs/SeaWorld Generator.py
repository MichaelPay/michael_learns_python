#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:12:59 2017

@author: hamsternation
"""




class sw:
    
    def __init__(self, userID):
        self.userID = userID
        self.cl = {}
        self.buyer = ''
        self.tix(input('how many tickets? '))
        self.inputter()
        self.isbuyer()
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        self.decider()
        input('Press any key to exit')

    def __len__(self):
        try:
            return self.tix
        except NameError or TypeError:
            return 0
    
    def __str__(self):
        pass
    
    def inputter(self):
        for x in range(self.tix):
            self.update('{}'.format(input('Please enter person number {} '.format(x+1))))
            
    def tix(self, tix):
        try:
            self.tix = int(tix)
        except ValueError:
            print('Sorry, but the number of tickets has to be a whole number! ')
    
    def update(self, Name):
        while len(Name.split(' ')) != 2:
            Name = input('Please enter the first and last name separated by a space! ')
        self.cl[len(self.cl)+1] = Name.title()
    
    def link(self):
        hotlink = []
        for value, key in self.cl.items():
            print('{}. {}'.format(value, key))
            item = '{}{}{}'.format(key[0].upper(),key.split(' ')[1],self.date())
            counter = 1
            while item in hotlink:
                item = '{}{}{}{}'.format(key[0].upper(),key.split(' ')[1],self.date(),'_' + str(counter))
                counter +=1
            print('http://tiny.cc/{} \n'.format(item))
            hotlink.append(item)

    def isbuyer(self):
        if input('Is the first name you\'re about to enter the name of the buyer? Y/n ') != 'n':
            self.buyer = self.cl[1]
        else:
            self.buyer = input('Please submit the first and last name of the buyer: ').title()
            
    def decider(self):
        if self.tix > 1:
            self.multiple_message()
        else:
            self.singular_message()

    def singular_message(self):
        print('''
Good afternoon {},

Thank you for your purchase. Your ticket is ready for download at the link below:

'''.format(self.buyer.split(' ')[0]))
        self.link()
        
        print('''

The ticket can be printed or displayed on your mobile device. You may proceed directly to the turnstile to be admitted to the park. The ticket is good for any day before December 30, 2017. Parking is not included.

Have a wonderful time at SeaWorld San Diego!
''')
    def multiple_message(self):
        print('''
Good afternoon {},

Thank you for your purchase. Your tickets are ready for download at the following links:

'''.format(self.buyer.split(' ')[0]))
        self.link()
        
        print('''

The tickets can be printed or displayed on your mobile devices. You may proceed directly to the turnstile to be admitted to the park. The tickets are good for any day before December 30, 2017. Parking is not included.

Have a wonderful time at SeaWorld San Diego!
''')

                
                
    @staticmethod
    def date():
        import datetime
        date = str(datetime.date.today()).split('-')
        date = ''.join(date[1:3])
        return date

sw(input('Please enter the UserName: '))