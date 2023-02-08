'''
Q140. Write a Python program to convert an integer to binary that keeps leading zeros.
Sample data : x=12
Expected output : 00001100
0000001100
'''
x = 12
print("By using bin function:", bin(x))
print(format(x, '08b'))
print(format(x, '010b'))
