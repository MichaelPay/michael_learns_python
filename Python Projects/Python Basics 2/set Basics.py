# -*- coding: utf-8 -*-

# Created on Sun Jul 23 16:13:20 2017

# @author: Monic

# creating a set
set({1,2,3})
# another way to create a set
{1,2,3}

# curly braces are dictionaries
type({})
# so typing
thing = {}
type(thing)

#should return 'dictionary'
#the following creates sets
set({})

print({1,22,12,3,4,23,23})
# returns the set in another order.

# add method

low_primes = {1,3,5,7,11,13}
low_primes.add(17)
low_primes.update({19,23},{2,29})
low_primes.add(15)
print(low_primes)
# gives a KeyError if doesn't exit:
try:
    low_primes.remove(100)
except KeyError:
    pass

# tries to remove, but no error
low_primes.discard(100)

set1 = set(range(10))
set2 = {1,2,3,5,7,11,13,17,19,23}
# finding union of 2 sets without having to change the sets
set1.union(set2)
set1 | set2

# finding difference between two sets
set1.difference(set2)
set2.difference(set1)
set1 - set2
set2 - set1

# symmetric difference, things that are unique to each sie
set1 ^ set2
set2.symmetric_difference(set1)

# intersection of the sets
set1.intersection(set2)
set1 & set2

# function to find out if sets 1 and 2 are supersets of each other
def superset(set1, set2):
    if set2-set1==set() and set1-set2!=set():
        print('The first set is a superset of the second set')
    elif set1-set2==set() and set2-set1!=set():
        print('The second set is a superset of the first set')
    elif set1-set2==set() and set2-set1==set():
        print('The two sets are the same')
    else:
        print('None of the sets are supersets of each other')

superset(set1,set2)