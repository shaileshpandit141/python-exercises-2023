'''
Q85. Write a Python program to check whether a file path is a file or a directory.
'''
from os.path import isdir, isfile

def file_or_directory(path):
    if isdir(path):  
        print("\nIt is a directory")  
    elif isfile(path):  
        print("\nIt is a normal file")  
    else:  
        print("It is a special file (socket, FIFO, device file)" )
    print()

if __name__=="__main__":
    path="abc.txt"  
    file_or_directory(path)
