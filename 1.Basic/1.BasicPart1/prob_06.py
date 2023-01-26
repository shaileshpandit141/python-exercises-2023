'''
Q6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''
def Accept_number():
    print("Enter the number seprated by comma (,).")
    var = input(":  ").split(',')
    print("List is ", list(var))
    print("Tuple is ", tuple(var))

if __name__=="__main__":
    Accept_number()