'''
Q68. Write a Python program to calculate sum of digits of a number.
'''
def sum_of_digits_of_number(number):
    number = str(number)
    temp = 0
    for i in number:
        temp += int(i)
    else:
        return temp

if __name__=="__main__":
    num = 123
    n = 1234
    print('Sum of digits of a number.', sum_of_digits_of_number(num))
    print('Sum of digits of a number.', sum_of_digits_of_number(n))

