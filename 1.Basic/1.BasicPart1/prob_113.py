'''
Q113. Write a Python program that inputs a number and generates an error message if it is not a number.
'''
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
		