"""Q5. Write a Python program to make combinations of 3 digits. """
numbers = []
for num in range(1000):
    num = str(num).zfill(3)
    # print(num) # This line print 001 to 999.
print('Last number is ', num)
numbers.append(num)
