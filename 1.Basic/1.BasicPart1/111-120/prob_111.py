'''
Q111. Write a Python program to make file lists from the current directory using a wildcard.
'''
import glob
file_list = glob.glob('*.*')
print(file_list)
#Specific files
print(glob.glob('*.py'))
print(glob.glob('./[0-9].*'))


# from pathlib import Path
# for path in Path("/").glob("*.*"):
#    print(path)
