'''
Q125. Write a Python program to sum all counts in a collection.
'''
import collections
from collections import Counter
num = [2,2,4,6,6,8,6,10,4]
print(sum(Counter(num).values()))

# you can also find by using len function.
print(len(num))
