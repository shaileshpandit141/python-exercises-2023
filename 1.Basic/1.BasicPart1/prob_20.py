'''
Q20. Write a Python program that returns a string that is n (non-negative integer) 
copies of a given string.
'''
def return_multple_str(text:str, num:int ):
    return text*num


if __name__=="__main__":
    print(return_multple_str('abc', 2))
    print(return_multple_str('.py', 3)) 
    