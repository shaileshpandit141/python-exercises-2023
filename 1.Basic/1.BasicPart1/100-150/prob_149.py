'''
Q149. Write a Python function that takes a positive integer and returns the sum of the cube of all 
positive integers smaller than the specified number.
'''
def sum_of_cubes(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n * n
        n -= 1
    return total
    
if __name__=="__main__":
    print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))
    