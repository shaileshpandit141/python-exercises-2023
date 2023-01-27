'''
Q18. Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.
'''
# from math import sum
def sumof_three_number(num1, num2, num3):
    
    if num1 == num2 == num3:
        return (num1 + num2 + num3)*3
    else:
        return num1 + num2 + num3

if __name__=="__main__":
    print(sumof_three_number(1, 2, 3))
    print(sumof_three_number(3, 3, 3))
