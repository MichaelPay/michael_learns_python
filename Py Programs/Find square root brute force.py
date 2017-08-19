x = 25
epsilon = 0.0001
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += 0.000001
    numGuesses += 1
print('Number of guesses to process this problem:' + str(numGuesses))
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(ans, ' is close to square root of ' + str(x))
