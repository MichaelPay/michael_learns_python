import random
import numpy
record = []
while True:
    try:
        high = int(input('Please put in the highest number in the guessing game: '))
        low = int(input('Please put in the lowest number in the guessing game: '))
        while low >= high:
            print('ERROR! Please make sure your low is lower than the high!')
            low = int(input('Please put in the lowest number in the guessing game: '))
        cycle = int(input('Please tell me how many times you would like the machine to guess using the algorithm: '))
        modulus = int(input('How many records before we ask you if you want to take a break? '))
        break
    except  ValueError:
        print('Please put in a valid  number! ')
        continue
    else:
        print('the low must be lower than the high!')
        continue

def main():
    global high
    global low
    number = random.randint(low,high)
    guesses = []
    indicator = 'high'
    while len(guesses) < cycle:
        if len(guesses) == 0:
            guess = int(numpy.mean([low,high]))
            if guess == number:
                guesses.append(guess)
                break
            elif guess > number:
                indicator = 'high'
                guesses.append(guess)
                continue
            else:
                indicator = 'low'
                guesses.append(guess)
                continue
        else:
            if indicator == 'high':
                guess = int(numpy.mean([guesses[-1],low]))
                if guess == number:
                    guesses.append(guess)
                    break
                elif guess > number:
                    indicator = 'high'
                    guesses.append(guess)
                    high = guess
                    continue
                else:
                    indicator = 'low'
                    guesses.append(guess)
                    low = guess
                    continue
            else:
                guess = int(numpy.mean([guesses[-1],high]))
                if guess == number:
                    break
                elif guess > number:
                    indicator = 'high'
                    high = guess
                    guesses.append(guess)
                    continue
                else:
                    indicator = 'low'
                    low = guess
                    guesses.append(guess)
                    continue
    print(guesses)
    print(number)
    print(guess)

main()
    