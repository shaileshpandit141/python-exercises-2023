'''
Q64. Write a Python program that retrieves the date and time of file creation and modification.
'''
from os.path import getmtime, getctime
from time import ctime

print("Last modified: %s" % ctime(getmtime("prob_60.py")))
print("Created: %s" % ctime(getctime("prob_60.py")))