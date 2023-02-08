'''
Q81. Write a Python program to concatenate N strings.
'''
list_of_colors = ['Red', 'White', 'Black']  

def join_String(StringList):
    j_string = ','.join(StringList)
    print()
    print("Join string list is: " + j_string)
    print()

if __name__=="__main__":
    join_String(list_of_colors)