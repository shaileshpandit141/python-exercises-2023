'''
Q132. Write a Python program to list the home directory without an absolute path.
'''
from os.path import expanduser
print(expanduser('~'))
