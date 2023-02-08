'''
Q121. Write a Python program to determine if a variable is defined or not.
'''
# let's consider first example.
try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")

# let's consider second example.
'''try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
  '''