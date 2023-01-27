'''
Q17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 
'''

def near_thousant(num):
    '''Test whether a number is within 100 of 1000 or 2000 '''
    return (abs(1000 - num) <= 100)  or (abs(2000 - num) <= 100)

if __name__=="__main__":
    print(near_thousant(1000))
    print(near_thousant(900))
    print(near_thousant(800))   
    print(near_thousant(2200))