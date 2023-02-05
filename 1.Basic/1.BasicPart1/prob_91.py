'''
Q91. Write a Python program to swap two variables.
'''
def swap_two_variables(num1, num2):
    num1 = num2
    num2 = num1
    # num1, num2 = num2, num1
    return (num1, num2)

if __name__=='__main__':
    n1 = 10
    n2 = 20
    print("\nBefore swap a = %d and b = %d" %(n1, n2))
    print("\nAfter swaping a = %d and b = %d" %swap_two_variables(n1, n2))