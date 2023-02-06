'''
Q49. Write a Python program to list all files in a directory.
'''

from os import system, listdir
from os.path import isfile, join

def list_all_files_in_directory():
    temp = '/home/panditjee/Desktop/PythonExercises/1.Basic/1.BasicPart1'
    files_list = [f for f in listdir(temp) if isfile(join(temp, f))]
    print(files_list)

if __name__=="__main__":
    list_all_files_in_directory()
