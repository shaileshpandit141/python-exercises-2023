'''
Q16. Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference. 
'''

def difference(number):
    if number <= 17:
        print('Absolute difference is:', abs(number-17))
    else:
        print('Twice difference is:', (number-17)*2)

if __name__=="__main__":
    n1 = 12
    n2 = 20
    difference(n1)
    difference(n2)
