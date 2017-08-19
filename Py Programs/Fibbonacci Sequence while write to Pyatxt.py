def findFib(s):
    """s is the number of cycles you would like the fibbonacci sequence to run for"""
    if s == 1 or s == 0:
        return 1
    else:
        return findFib(s-1) + findFib(s-2)

def testFib(n):
    for i in range(n+1):
        if i == 0 or i == 1:
            fob=open('c:/Py/a.txt', 'w')
        print('Sequence', i, 'of the fibbonacci sequence is ', findFib(i))
        fob.write('Sequence ')
        fob.write(str(i))
        fob.write(' of the fibbonacci sequence is ')
        fob.write(str(findFib(i)))
        fob.write("\n")
    fob.close()
testFib(int(input('How many steps of the fibbonacci sequence would you like to calculate? (up to 32)')))

while int(input('press any button to continue, or 1 to do another calculation:')) == int(1):
    testFib(int(input('How many steps of the fibbonacci sequence would you like to calculate? (up to 32)')))
else:
    None

