'''
Q134. Write a Python program to input two integers on a single line.
'''
print("Input the value of x & y")
try:
    x_num, y_num = map(int, input(':    ').split())
    print("The value of x & y are: ",x_num, y_num)
except Exception as e:
    print(e)