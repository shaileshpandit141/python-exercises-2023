'''
Q31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
'''
def greatest_common_divisor(num1:int, num2:int):
    if num2 > num1:
        mn = num1
    else:
        mn = num2
    for i in range(1, mn+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    print("The greatest common divisor is:", gcd)

if __name__=="__main__":
    print("Please! Enter two number to find its greatest common divisor.")
    n1 = int(input(":   "))
    n2 = int(input(":   "))
    greatest_common_divisor(n1, n2)