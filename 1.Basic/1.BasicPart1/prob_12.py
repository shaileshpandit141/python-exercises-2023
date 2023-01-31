'''
Q12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
'''

import calendar

def Print_calender():
    print("Please! Enter month and year to print calender.")
    month = int(input("Month: "))
    Year = int(input("Year: "))
    return calendar.month(Year,month)


if __name__=='__main__':
    A = Print_calender()
    print()
    print(A)
    