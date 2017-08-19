# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:22:41 2017

@author: Monic
"""

# Regular Expressions

# import the regular expressions library
import re

# opens the names file,
# reads and loads it into the data variable
# closes the file
#
names_file = open('names.txt', encoding = "utf-8")
data = names_file.read()
names_file.close()

#print(data)

# parsing through data
#
#print(re.match(r'Love', data))
#print(re.match(r'Kenneth', data))
#print(re.search(r'Kenneth', data))

# the r in string represents a raw string

#print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d',data))

# Count library:
# . matches any character except new line
# \w unicode word character
# \W anything that isn't a unicode word
# \s whitespace
# \S anything that isn't whitespace
# \d any number 0 to 9
# \D anything that isn't a number
# \b word boundaries or edges of a word
# \B anything that isn't a word boundary

# finds a letter 1 to infinity number of times a comma,
# and another letter 1 to infinity times
#print(re.findall(r'\w+, \w+', data))

#print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}',data))

# {3} something occurs exactly 3 times
# {,3} 0 - 3 times
# {3,5} 3-5 times
# ? occurs 0 or 1 times
# * occurs 0 to infinity times
# + occurs 1 to infinity times

#casting a variable as a string into the 
# count formula

#import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']
# finds count or more number of words
#def find_words(count, stringy):
#    return re.findall(r'\w{'+ str(count) +',}', stringy)


# sets
# [aple] matches apple
# [a-z] any lower letter from a - z
# [^2] anything that is not 2, a pattern doesn't have a 2
# ignorecase flag
# verbose flat - write pattern in a natural way
# parsing email
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+.[\w\d+]+', data))
# ignorecase , also "re.I" works too
#print(re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))

# email address, except addresses that end in .gov

# verbose characters:
#print(re.findall(r'''
#                 \b@[-\w\d.]* # First a word boundary, an @ and then any # of characters
#                 [^gov\t]+ # ignore 1+ instances of the letters 'g','o','v' and a tab
#                 \b # match another word boundary
#''', data, re.VERBOSE | re.I))
#
#print(re.findall(r"""
#              [-\w]*, # find a word boundary, 1+ hyphens or characters, and a comma
#              \s # Find 1 whitespace
#              [-\w ]+ # 1+ hyphens and characters and explicit spaces
#              [^\t\n] # ignore tabs and new lines
#""", data, re.X))

# Grouping
#line = re.search(r'''
#                 ^(?P<name>[-\w ]*,\s[-\w ]+)\t # last and first names
#                 (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # email
#                 (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Jobs and Company
#                 (?P<job>[\w\s]+,\s[\w\s.]+)\t?
#                 (?P<twitter>@[\w\d]+)?$ # Twitter
#''', data, re.X|re.M)
#
#print(line)
#print(line.groupdict())

#Challenge
#
#string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
#Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
#McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
#Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''
#
#contacts = re.search(r'''
#    ^[\w]+,\s[\w]+,\s
#    (?P<email>[\w+.]*@[\w.]*)
#    ,\s
#    (?P<phone>\d{3}-\d{3}-\d{4})
#    ,\s
#    @[\w]+$
#''', string, re.X|re.I|re.M)
#
#twitters = re.search(r'''
#    @[\w]+$
#''', string, re.X|re.M)

# compiling regular expression

line = re.compile(r'''
                 ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # last and first names
                 (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # email
                 (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Jobs and Company
                 (?P<job>[\w\s]+,\s[\w\s.]+)\t?
                 (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X|re.M)

print(re.search(line, data).groupdict())
print(line.search(data).groupdict())

for match in line.finditer(data):
    print(match.group('name'))

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))

