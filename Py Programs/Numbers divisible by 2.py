x = int(input('Enter something here'))
if x%2 == 0:
    print('even')
else:
    print('odd')
    if x%3 != 0:
        print('And not divisible by 3')
