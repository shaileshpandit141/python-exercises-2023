'''
Q70. Write a Python program to sort files by date.
'''
from glob import glob
from os.path import getmtime

files = glob("*.py")
files.sort(key=getmtime)
print("\n".join(files))
