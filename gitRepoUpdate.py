import sys
import os
from pathlib import Path
import subprocess

path = os.getcwd()
try:
    path = Path(path, sys.argv[1])
except IndexError:
    pass
path = Path(path).resolve()

print(subprocess.run('git', stdout= subprocess.PIPE).stdout.decode("utf-8"))