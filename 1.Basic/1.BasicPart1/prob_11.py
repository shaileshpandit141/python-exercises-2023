'''
Q11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

def abs(number):
    '''Return the absolute value of the argument.'''
    return number

if __name__=="__main__":
    print(abs.__doc__)
    print("Absolute value of the argument is: ",abs(5))
