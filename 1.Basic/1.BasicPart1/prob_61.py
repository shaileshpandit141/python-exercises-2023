'''
Q61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. 
'''

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print(f"The distance in inches is {d_inches} inches.")
print(f"The distance in yards is {round(d_yards, 5)} yards.")
print(f"The distance in miles is {round(d_miles, 5)} miles.")
