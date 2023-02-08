'''
Q146. Write a Python program to find the location of Python module sources.
'''
from imp import find_module
print("Location of Python os module sources:")
print(find_module('os'))
print("\nLocation of Python sys module sources:")
print(find_module('datetime'))
