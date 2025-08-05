import shutil
from pathlib import Path
h = Path.home()
#copies the file from ~/spam folder to ~ folder
shutil.copy(h / 'spam/fil1.txt', h)
#copies fil1.txt to same dir as fil2.txt 
shutil.copy(h / 'spam/fil1.txt', h / 'spam/fil2.txt')