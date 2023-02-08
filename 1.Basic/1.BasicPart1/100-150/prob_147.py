'''
Q147. Write a Python function to check whether a number is divisible by another number. Accept two 
integer values from the user.
'''
def multiple(m, n):
	return True if m % n == 0 else False

if __name__=="__main__":
    print(multiple(20, 5))
    print(multiple(7, 2))
