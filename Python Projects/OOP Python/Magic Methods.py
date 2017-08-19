# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:52:49 2017

@author: Monic
"""

# Magic Methods

class Characters:
    
    def __init__(self, name = "test", **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)

Michael = Characters()
print(Michael)

# numstring.py
# a class that holds a float or int as a string
# but allows us to turn it back into an int whenever we want to
class NumString:
    def __init__(self, value):
        self.value = str(value)
    def __str__(self):
        return self.value
    def __int__(self):
        return int(self.value)
    def __float__(self):
        return float(self.value)

five = NumString(5)
print(str(five))
print(int(five))
print(float(five))



# challenge
# Let's use __str__ to turn Python code into Morse code! OK, not really, but we can turn class instances into a representation of their Morse code counterparts.
# I want you to add a __str__ method to the Letter class that loops through the pattern attribute of an instance and returns "dot" for every "." (period) and "dash" for every "_" (underscore). Join them with a hyphen.
# I've included an S class as an example (I'll generate the others when I test your code) and it's __str__ output should be "dot-dot-dot".

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self):
        answer = []
        for x in self.pattern:
            if x == '.':
                answer.append('dot')
            if x == '_':
                answer.append('dash')
            else:
                continue
        return '-'.join(answer)
                              
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)