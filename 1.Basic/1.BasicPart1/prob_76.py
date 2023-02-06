'''
Q76. Write a Python program to get the command-line arguments (name of the script, the number 
of arguments, arguments) passed to a script.
'''
from sys import argv
temp = argv[0]
print("This is the name/path of the script:",temp)
print("Number of arguments:",len(argv))
print("Argument List:",str(argv))
