# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:38:20 2017

@author: Monic
"""

# __new__ is used to modify immutable data types

class rStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self
    
# creating subclass for mutable objects
# allows a copy of lists
import copy

class FilledList(list):
    # __init__ accepts 2 new values than the super
    def __init__(self, count, value, *args, **kwargs):
        # creates an empty list stored in self
        # passing the super argument
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))
            
my_list = FilledList(9, [3,4,5,6,8])
print(my_list)

# create a subclass of list that always returns the wrong 
# length when asked for length

class Liar(list):
    def __len__(self, *args, **kwargs):
        super().__len__()
        self = len(args)
        return self

nice = Liar([1,2,3,4])
print(len(nice))