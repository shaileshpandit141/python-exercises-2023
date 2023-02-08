'''
Q52. Write a Python program to print to STDERR.
'''
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if __name__=="__main__":
    eprint("abc", "efg", "xyz", sep="--")
