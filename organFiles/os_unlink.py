import os
from pathlib import Path
myHome = (Path.home() / 'spam')


for filename in myHome.glob('*.txt'):
    print('Deleting: ', filename)
    os.unlink(filename)
    #print(filename, + ' Deleted')
#use os.unlink to delete a fine at a path
print(myHome)
