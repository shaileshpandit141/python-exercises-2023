'''
Q10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5
Expected Result : 615
'''
def Accepts_integer(num):
    print('The value of n+nn+nnn is: ', num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num)))

if __name__=="__main__":
    n = 5
    Accepts_integer(n)
    