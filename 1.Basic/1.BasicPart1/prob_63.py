'''
Q63. Write a Python program to get an absolute file path. 
'''
from os.path import abspath

def absolute_file_path(path_fname):
    return abspath(path_fname)    

print("Absolute file path: ",absolute_file_path("./"))
