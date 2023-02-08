'''
Q141. Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04
'''
def convt_Hex(num):
    if len(hex(num))>=4:
        print(hex(num)[2:])
    else:
        print("0" + hex(num)[2:])
   

if __name__=='__main__':
    n1, n2 = 30, 4
    convt_Hex(n1)
    convt_Hex(n2)