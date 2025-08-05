import shutil
from pathlib import Path
h = Path.home()
#copies all files in a dir to another dir
(h / 'spam2').mkdir(exist_ok=True)
shutil.move( h / 'spam/file1.txt', h / 'spam2/file1.txt')
