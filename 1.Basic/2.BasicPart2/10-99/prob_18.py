"""Q18. Write a Python program to find the median among three given numbers.
"""
x = input("Input the first number:  ")
y = input("Input the second number: ")
z = input("Input the third number:  ")
print("Median of the above three numbers -")

if y < x < z:
    print(x)
elif z < x < y:
    print(x)

elif z < y < x:
    print(y)
elif x < y < z:
    print(y)

elif y < z < x:
    print(z)
elif x < z < y:
    print(z)
