'''
Q82. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary). 
'''

def sum_of_container(my_cont):
    temp = 0
    if type(my_cont) != dict: 
        for it in my_cont:
            temp += it
        else:
            return temp
    elif type(my_cont) == dict:
        for i in my_cont:
            temp += my_cont[i]
        else:
            return temp
    else:
        print("Somthing is Wrong.")


if __name__=="__main__":
    tup = (1, 2, 3)
    li = [1, 2, 3]
    se = {1, 2, 3}
    dic = {1:1, 2:2, 3:3}

    print(f"Sum of tuple is {sum_of_container(tup)}")
    print(f"Sum of list is {sum_of_container(li)}")
    print(f"Sum of set is {sum_of_container(se)}")
    print(f"Sum of dictionary is {sum_of_container(dic)}")
