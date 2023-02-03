'''
Q87. Write a Python program to get the size of a file.
'''
from os.path import getsize

try:
    file_size = getsize("prob_87.py")
    print("\nThe size of abc.txt is :",file_size,"Bytes")
    print()
except Exception as e:
    print(e)
