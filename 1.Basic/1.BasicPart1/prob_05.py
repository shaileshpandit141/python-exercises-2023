'''
5. Write a Python program that accepts the user's first and last name and prints them in
reverse order with a space between them.
'''
def Accept_user_name():
    print("Please! Enter your first and second name.")
    first_name = input(":   ")
    last_name = input(":   ")
    print('In reverse order:',last_name, first_name)

if __name__=="__main__":
    Accept_user_name()
    