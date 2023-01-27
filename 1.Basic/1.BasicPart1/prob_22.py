'''
Q22. Write a Python program to count the number 4 in a given list. 
'''
def count_duplicate_values(mylist, num):
    count = 0
    for i in mylist:
        if i == num:
            count += 1
        else:
            pass
    else:
        print(num, 'repated by', count, 'times in your list :',mylist)

if __name__=="__main__":
    number = 4
    count_duplicate_values([1, 4, 6, 4, 7, 4], number)
    count_duplicate_values([1, 4, 6, 7, 4], number)
    count_duplicate_values([1, 4, 6, 7, 4, 4, 4, 5], number)