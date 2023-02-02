'''
Q73. Write a Python program to calculate the midpoints of a line.
'''
def midpoints(point1, point2):
    x_point = (point1[0] + point2[0])/2
    y_point = (point1[1] + point2[1])/2
    return [x_point, y_point]

if __name__=="__main__":
    p1 = [ int(i) for i in input(" Enter first point seprated by ,: ").split(",")]
    p2 = [ int(i) for i in input("Enter second point seprated by ,: ").split(",")]
    print( "The midpoint is: ",midpoints(p1, p2))