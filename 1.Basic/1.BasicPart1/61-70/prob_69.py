'''
Q69. Write a Python program to sort three integers without using conditional statements and loops.
'''
num1 = int(input(" Input first number: "))
num2 = int(input("Input second number: "))
num3 = int(input(" Input third number: "))

A1 = min(num1, num2, num3)
A2 = max((num1, num2, num3))
A3 = num1 + num2 + num3 - A1 - A2
print("Numbers in sorted order: ", A1, A2, A3)