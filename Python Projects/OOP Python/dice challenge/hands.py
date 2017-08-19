#Now update Hand in hands.py. I'm going to use code similar to Hand.roll(2) 
# and I want to get back an instance of Hand with two D20s rolled in it. 
#I should then be able to call .total on the instance to get the total of the two dice.
#I'll leave the implementation of all of that up to you. 
#I don't care how you do it, I only care that it works.

import dice

class Hand(list):

    def __init__(self, size=0, die_class=None):
        super().__init__()
        for _ in range(size):
            self.append(die_class())

    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, size):
        return cls(size, die_class=dice.D20)