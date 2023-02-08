'''
Q33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero. 
'''
def print_sum_ofthree(num1:int, num2:int, num3:int):
    test = (num1, num2, num3)
    if num1 == num2 or num2 == num3 or num1 == num3:
        return 0
    else:
        return num1 + num2 + num3

if __name__=="__main__":
    print(print_sum_ofthree(2, 1, 2))
    print(print_sum_ofthree(3, 2, 2))
    print(print_sum_ofthree(2, 2, 2))
    print(print_sum_ofthree(1, 2, 3))
