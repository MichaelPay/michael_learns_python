# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:28:17 2017

@author: Monic
"""

listing = 'Hello, How are you today? I am so cool! Nice to meet you, son!'
my_list = listing.split()
for word in my_list:
    print(word)

for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(letter.upper())

#create a list with the number 1 in it
list_of_num = [1]
#appends numbers to end of the list called list_of_num
for x in range(1,100):
    list_of_num.append(list_of_num[-1] + 1)

#find all the even numbers in the list and print them
for num in list_of_num:
    if num % 2 == 0:
        print(num)
        
#while loop countdown from 1000 to 0
start = 1000
while start:
    print(start)
    start -= 1
print(0)