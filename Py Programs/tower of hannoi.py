fob=open('c:/Py/a.txt', 'w')
def Hannoi(n, f, t, s):
    if n == 1:
##        print(f + t)
        fob.write('Move piece from the "')
        fob.write(str(f))
        fob.write('" pile to the "')
        fob.write(str(t))
        fob.write('" pile.')
        fob.write("\n")

    else:
        Hannoi(n-1, f, s, t)
        Hannoi(1, f, t, s)
        Hannoi(n-1, s, t, f)
