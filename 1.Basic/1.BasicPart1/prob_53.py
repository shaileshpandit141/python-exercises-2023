'''
Q53. Write a Python program to access environment variables.
'''
from os import environ
# Access all environment variables 
print('*----------------------------------*')
print(environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(environ['HOME'])
print('*----------------------------------*')
print(environ['PATH'])
print('*----------------------------------*')
