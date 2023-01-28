"""
Q40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""
from math import sqrt
def distance_between_points(point1:float, point2:float):
    return sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


if __name__=='__main__':
    p1 = [4, 0]
    p2 = [6, 6]
    print("Distance between two points :",distance_between_points(p1, p2))