'''
Q39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''

def future_value(amount:int, int_:float, years:int):
    return amount * ((1 + (0.01 * int_)) ** years)


if __name__=="__main__":
    amt = 10000
    int_ = 3.5
    years = 7
    print(future_value(amt, int_, years))
    print(round(future_value(amt, int_, years),2))
