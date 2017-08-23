import os

# get current working directory
os.getcwd()

# navigate to new location in file system
os.chdir('/home/hamsternation/Desktop')

# lists the directory
os.listdir()

# scan dir
list(os.scandir())


# create a new directory (single level)
os.mkdir('testing')

# create new directory (multiple level)
os.makedirs('testing/lots of tests')

# remove single level dir
os.rmdir('testing')

# remove multiple level (recursively) directories
os.removedirs('testing/lots of tests')

# renaming files
os.rename('testing.txt', 'new_name.txt')

# file stats, such as date, size of the file.
os.stat('testing.txt')

# directory walk from bottom level up
# results in a 3 value tuple of (dirpath, dirsinpath, filesinpath)

os.walk()
# example
for cur, pathlist, filelist in os.walk('/'):
    print('Current Directory: ', cur)
    print('Directories in current directory: ', pathlist)
    print('Files in current directory: ', filelist)
    print('\n\n\n')

# joining paths together
os.path.join(os.environ.get('HOME'), 'test.txt')

# prints basename of file
os.path.basename('/tmp/test.txt')
# prints text.txt

os.path.dirname('/tmp/test.txt')

os.path.splitext('/temp/test.txt')
# splits to ('/tmp/test', '.txt')

os.path.isabs('/home/hamsternation/Desktop')

# pathlib

import pathlib

path = pathlib.PurePath(os.getcwd())
path2 = path / 'examples' / paths.txt
print(path2.parts,
      path2.root,
      path2.name,
      path2.suffix)

