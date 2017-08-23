import os

def dir_contains(path, listnames):
    booly = []
    for x in listnames:
        if x in os.listdir(path):
            booly.append('True')
        else:
            booly.append('False')
    return not 'False' in booly