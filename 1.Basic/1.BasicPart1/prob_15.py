'''
Q15. Write a Python program to get the volume of a sphere with radius six.
'''
from math import pi
def volume_of_sphere(radius):
    print("The volume of a sphere is: ",(4/3)*pi*(radius**3))

if __name__=="__main__":
    radius = float(input("Please! Enter radius to find valum os a sphere: "))
    volume_of_sphere(radius)
    