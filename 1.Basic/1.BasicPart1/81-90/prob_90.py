'''
Q90. Write a Python program to create a copy of its own source code.
'''
from shutil import copy

# Copy file example.txt into a new file called example_copy.txt
copy('main.py', 'example_copy.py')

# Copy file example.txt into directory test/
copy('example.txt', 'test/')