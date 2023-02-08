'''
Q145. Write a Python program to test if a variable is a list, tuple, or set. 
'''
def test(ty):
    if type(ty) in (list, tuple, set):
        return f'{ty} is {type(ty)}'
    else:
        return False

if __name__=="__main__":
    x1 = ['a', 'b', 'c', 'd']
    x2 = {'a', 'b', 'c', 'd'}
    x3= ('tuple', False, 3.2, 1)
    print(test(x1))
    print(test(x2))
    print(test(x3))
