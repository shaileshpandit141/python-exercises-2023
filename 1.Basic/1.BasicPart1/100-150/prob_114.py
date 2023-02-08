'''
Q114. Write a Python program to filter positive numbers from a list. 
'''

def p_number_inlist(mylist):
    temp_list = []
    for i in mylist:
        if i >= 0:
            temp_list.append(i)
        else:
            pass
    else:
        return sorted(temp_list)

if __name__=="__main__":
    li = [1, 2, -3, 3, 4, 6, 5, -5, -6]
    print(p_number_inlist(li))


    '''
    nums = [34, 1, 0, -23, 12, -88]
    print("Original numbers in the list: ",nums)
    new_nums = list(filter(lambda x: x >0, nums))
    print("Positive numbers in the said list: ",new_nums)
    '''