'''
Q66. Write a Python program to calculate the body mass index.
'''
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height ** 2), 2))
