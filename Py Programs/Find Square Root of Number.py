x = float(input('Choose a number to find the square root of: '))
epsilon = 0.0000000000001
numGuesses = 0
low = 0.0
high = max(x, 1)
ans = (high + low)/2
while abs(ans**2 - x) >=epsilon and ans <= x:
    print(str(low), str(high),str(ans))
    numGuesses += 1
    if ans**2 <x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('Number of guesses taken to solve this problem: ', str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))
input('Press any key to exit')
