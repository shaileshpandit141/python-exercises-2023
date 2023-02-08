'''
Q142. Write a Python program to check if every consecutive sequence of zeroes is followed by a 
consecutive sequence of ones of same length in a given string. Return True/False.

Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 000111000111
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00011100011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
'''
def test(str1):
    while '01' in str1:
        str1 = str1.replace('01', '')
    return len(str1) == 0

str1 = "01010101"
print("Original sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
