'''
Q58. Write a Python program to sum the first n positive integers.
'''

def sum_of_npositive(n:int):
    n_sum = 0
    for i in range(1, n+1):
        n_sum += i
    return n_sum
def method_02(n:int):
    sum_n = (n * (n + 1)) / 2
    return sum_n

if __name__=="__main__":
    num = int(input("Please! Enter one number to print its sum: "))
    print(sum_of_npositive(num))
    print(method_02(num))
