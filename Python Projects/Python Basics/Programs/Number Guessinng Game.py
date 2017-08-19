# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 22:20:38 2017

@author: Monic
"""

import random

def main():
    number = random.randint(1,10)
    print('\n'*80)
    guesses = []
    print("Hello petty human, I am thinking of a number from 1 to 10 in my head, you have 5 tries to guess it or else I will destroy the world. Go ahead, the fate of the world in your hand!")
    while len(guesses) < 5:
        try:
            human_guess = int(input('\nGuess a number from 1 to 10!'))
        except ValueError:
            print('\nThat\'s not a real number!')
            continue
        else:
            if human_guess == number:
                print("\nLucky you. Looks like you have guessed the number I was thinking off, which was {}. You have saved humanity!".format(number))
                break
            elif human_guess > number:
                print("\nThat number is way too large! You have " + str(4-len(guesses)) + " chances left!")
            else:
                print("\nThat number is way too small! You have " + str(4-len(guesses)) + " chances left!")
        guesses.append(human_guess)
    else:
        print('\nYou\'re all out of chances!! The number was {}!!! Human race has now been destoryed!! muahhahahhah'.format(number))
    if input('\nDo you want to play again? Type "Yes" to play.').lower() == "yes":
        main()
    else:
        print("\nOk! Bye!")

main()

    
    

