'''
Q144. Write a Python program to check whether a variable is an integer or string.
'''
var1 = "Hello"
var = 123
if type(var) == int:
    print(f"Given data {var} is a integer.")
elif type(var) == str:
    print(f"Given data {var} is a string.")
else:
    print(f"data {var} are not integer and string.")