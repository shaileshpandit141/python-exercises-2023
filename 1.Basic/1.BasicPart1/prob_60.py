'''
Q60. Write a Python program to calculate the hypotenuse of a right angled triangle.
'''
from math import sqrt

def hypotenuse_of_right_angled_triangle(base:float, height:float):
    hypotenuse = sqrt(base**2 + height**2)
    return hypotenuse


if __name__=="__main__":
    print("Please! Enter base and height to calculate hypotenuse of a right angled triangle.")
    b = float(input("Base:    "))
    h = float(input("Height:    "))
    print("Hypotenuse of a right angled triangle is: ", hypotenuse_of_right_angled_triangle(b, h))
