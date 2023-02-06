'''
Q35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
'''

def if_return_true(num1:int, num2:int):
    if (num1 == num2) or (num1 + num2 == 5) or (num1 - num2 == 5):
        return True
    else:
        pass

if __name__=="__main__":
    print(if_return_true(7, 2))
    print(if_return_true(3, 2))
    print(if_return_true(2, 2))
    print(if_return_true(7, 3))
    print(if_return_true(27, 53))
