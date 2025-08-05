import shutil
from pathlib import Path
h = Path.home()
#copies all files in a dir to another dir

shutil.copytree( h / 'spam', h / 'spam_backup')
