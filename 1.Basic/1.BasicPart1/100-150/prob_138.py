'''
Q138. Write a Python program to convert true to 1 and false to 0.
'''

def convt(var):
    temp = 0 if var==False else 1
    return temp

if __name__=='__main__':
    var = False
    print(convt(var))
    var = True
    print(convt(var))
