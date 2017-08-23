def rememberer(thing):
    with open('database.txt', 'a') as file:
        file.write(thing+"\n")


if __name__ == '__main__':
    rememberer(input('What should I get? \n'))
