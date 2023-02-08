'''
Q136. Write a Python program to find files and skip directories in a given directory. 
'''
from os import listdir
from os .path import isfile, join

def display_files_name(uname):
    print([f for f in listdir(f'/home/{uname}') if isfile(join(f'/home/{uname}', f))])

if __name__=='__main__':
    try:
        user = 'students'
        display_files_name(user)
    except Exception as e:
        print(e)