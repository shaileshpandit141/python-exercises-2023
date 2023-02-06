'''
Q34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
'''
def check_between(sum:int):
    if sum > 15 and sum < 20:
        return 20
    else:
        return sum

def print_sum_oftwo(num1, num2):
    return(check_between(num1 + num2))

if __name__=="__main__":
    print(print_sum_oftwo(10, 6))
    print(print_sum_oftwo(10, 2))
    print(print_sum_oftwo(10, 12))
    