'''
Q41. Write a Python program to check whether a file exists.
'''
from os import path

# method 01
def file_exist_or_not_01(file_name):
    print(path.exists(file_name))

# method 02
def file_exist_or_not_02(file_name):
    print(path.isfile(file_name))
    print(path.isfile(file_name))

# method 03
def file_exist_or_not_03(file_name):
    my_file = open(file_name)
    try:
        my_file.close()
        print("File found!")
    except FileNotFoundError:
        print("File not found!")

if __name__=="__main__":
    file_exist_or_not_01("prob")
    file_exist_or_not_01("prob_01.py")
