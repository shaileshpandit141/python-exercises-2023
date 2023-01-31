'''
Q4. Write a Python program that calculates the area of a circle based on the radius entered by the user. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
from math import pi
def CricleArea(r):
    print('Area of circule is: ', pi*(r**2))

if __name__=="__main__":
    r = float(input("Enter the the radious of circle: "))
    CricleArea(r)
    