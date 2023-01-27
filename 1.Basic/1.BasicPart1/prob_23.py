'''
Q23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of 
a given string. Return n copies of the whole string if the length is less than 2.
'''
def substring_copy(text:str, num:int):
    var = 2
    if var > len(text):
        var = len(text)

    substr = text[:var]
    result = substr*num
    print(result)

if __name__=='__main__':
    substring_copy('abcdef', 2)
    substring_copy('pkjdskvbakl', 3)
    substring_copy('', 5)
    substring_copy('abs', 1)

