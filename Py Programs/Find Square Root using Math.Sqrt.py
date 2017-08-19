import math
print(math.sqrt(float(input('Find the square root of: '))))
while input('Press any key to exit, "1" to Calculate another square root ') == str(1):
    print(math.sqrt(float(input('Find the square root of: '))))
else:
    None
