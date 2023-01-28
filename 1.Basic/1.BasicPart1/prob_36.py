'''
Q36. Write a Python program to add two objects if both objects are integers.
'''
def add_int_numbers(num1, num2):
    if (type(num1) == int) and (type(num2) == int):
        return num1 + num2
    else:
        return "Please! Enter only integers number."


if __name__=="__main__":
    print(add_int_numbers(10, 20))
    print(add_int_numbers(10, 20.23))
    print(add_int_numbers('5', 6))
    print(add_int_numbers('5', '6'))
