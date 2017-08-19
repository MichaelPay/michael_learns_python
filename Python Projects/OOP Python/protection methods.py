# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 20:16:42 2017

@author: Monic
"""

# Special methods such as protection

class Protected:
    __name = "Security"
    def __method(self):
        return self.__name



prot = Protected()
# the following yields error
#prot.__name

# the following yields error as well
#prot.__method()


# a print directory shows that the names with 
# dunder in front are name-mangled
# to be _Protected__name

print(dir(prot))

print(prot._Protected__name)
print(prot._Protected__method())

