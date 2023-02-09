"""Q7. Write a Python program to count the number of each character in a text file."""
import collections
import pprint

file_input = input('File Name: ')
with open(file_input, 'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)
print(value)
