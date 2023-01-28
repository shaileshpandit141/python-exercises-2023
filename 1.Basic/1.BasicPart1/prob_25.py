'''
Q25. Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False                                      
'''
def check_contain_ornot(mylist:int, number:int):
    if number in mylist:
        return True
    else:
        return False

if __name__=="__main__":
    n1 = 3
    l1 = [1, 5, 8, 3]
    print(check_contain_ornot(l1, n1))

    n2 = -1
    l2 = [1, 5, 8, 3]
    print(check_contain_ornot(l2, n2))