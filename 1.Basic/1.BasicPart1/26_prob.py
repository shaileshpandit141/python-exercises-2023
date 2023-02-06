'''
Q26. Write a Python program to create a histogram from a given list of integers.
'''

def print_histogram(group_data:int):
    for i in group_data:
        for i in range(i):
            print("*",end='')
        else:
            print()
    
if __name__=="__main__":
    data = [2, 3, 6, 5]
    print_histogram(data)

    print()
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_histogram(data1)
    