'''
Q21. Write a Python program that determines whether a given number (accepted from the user) 
is even or odd, and prints an appropriate message to the user.
'''
def even_or_odd(num:int):
    if num%2==0:
        print(f"Given number {num} is Even number.")
    else:
        print(f"Given number {num} is Odd number.")


if __name__=="__main__":
    print("Enter a number to find its even or odd.")
    num = int(input(":  "))
    even_or_odd(num)
    