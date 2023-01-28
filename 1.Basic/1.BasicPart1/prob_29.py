'''
Q29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output : {'Black', 'White'}
'''

def print_colour(colour_data1, colour_data2):
    print(colour_data1),print(colour_data2)
    print()

    print("Differenct of color_list_1 and color_list_2:")
    print(color_list_1.difference(color_list_2))

    print("Differenct of color_list_2 and color_list_1:")
    print(color_list_2.difference(color_list_1))

if __name__=="__main__":
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print_colour(color_list_1, color_list_2)