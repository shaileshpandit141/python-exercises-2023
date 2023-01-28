'''
Q30. Write a Python program that will accept the base and height of a triangle and compute its area.
'''

def area_of_tringle(base:float, height:float):
    print("Area of tringle is :", (1/2)*base*height)

if __name__=="__main__":
    print("Please! Enter base and height to calculate area of triangle.")
    Base = int(input("Base:   "))
    Height = int(input("Height:   "))
    area_of_tringle(Base, Height)