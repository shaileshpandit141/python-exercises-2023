'''
Q27. Write a Python program that concatenates all elements in a list into a string and returns it.
'''

def concatenate_list_data(group_data):
    var = ""
    for i in group_data:
        var += str(i)
    else:
        return var

if __name__=='__main__':
    print(concatenate_list_data([1, 5, 12, 2]))
    print(concatenate_list_data(["A", 5, "X", 2]))
    