# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:46:11 2017

@author: Monic
"""

# list like class creation

class Inventory:
    def __init__(self):
        self.slots = []
    def add(self, item):
        self.slots.append(item)
    # allows the class to accept len()
    def __len__(self):
        return len(self.slots)
    # allows the class to accept str()
    def __str__(self):
        return str(self.slots)
    # allows the class to utilize the item in self
    
    def __contains__(self, item):
        return item in self.slots
    # allows the class to utilize the iter method
    def __iter__(self):
            # yield is a generator that doesn't
            # terminate the execution of the method
            # but generates solutions
            # and keep working til the end
            # this code is the same as a for loop
            # for x in self.slot:
            #     yield x
            yield from self.slots
            
food = Inventory()
food.add('goodies')
food.add('things')
food.add('yummies')
print(len(food))
print(food)

if 'things' in food:
    print('yes, it\'s in food')

for item in food:
    print(item)