'''
Q143. Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit 
mode on the operating system. 
'''
from struct import calcsize
print(calcsize("P") * 8)
