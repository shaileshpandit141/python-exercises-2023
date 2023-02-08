'''
Q78. Write a Python program to find the available built-in modules.
'''
from sys import builtin_module_names
from textwrap import fill

print(builtin_module_names)
module_name = ', '.join(sorted(builtin_module_names))
# print(module_name)
# print(fill(module_name, width=70))
