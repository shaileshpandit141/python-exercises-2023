'''
Q47. Write a Python program to find out the number of CPUs used.
'''

from multiprocessing import cpu_count
print("Number of CPUs:", cpu_count())
