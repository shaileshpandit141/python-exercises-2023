'''
Q8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
def Disply_fistlast_colours(mycolor_list):
    print('First colour is:', mycolor_list[0])
    print('First colour is:', mycolor_list[len(mycolor_list)-1])

if __name__=="__main__":
    color_list = ["Red","Green","White" ,"Black"]
    Disply_fistlast_colours(color_list)
    