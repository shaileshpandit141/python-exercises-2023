'''
Q83. Write a Python program to test whether all numbers in a list are greater than a certain number.
'''
num = [2, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()
