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


def checkIsModules():
    hasModules = False
    console_out = subprocess.run('cat .gitmodules', stdout=subprocess.PIPE).stdout.decode("utf-8")
    if 'No such file or directory' not in console_out:
        hasModules = True
    return hasModules


ifSubmodule = checkIsModules()
(subprocess.run('cat .gitmodules', stdout=subprocess.PIPE).stdout.decode("utf-8"))
print(subprocess.run('git fetch', stdout=subprocess.PIPE).stdout.decode("utf-8"))
print(subprocess.run('git remote prune origin', stdout=subprocess.PIPE).stdout.decode("utf-8"))

