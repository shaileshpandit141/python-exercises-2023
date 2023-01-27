'''
Q19. Write a Python program to get a newly-generated string from a given string where "Is" has 
been added to the front. Return the string unchanged if the given string already begins with "Is".
'''

def new_string(text:str):
    # text = text.lower()
                        # text.startwith("is")text[:2] == "is"
    if len(text) >= 2 and (text.startswith("is") or text.startswith("Is")):
        return text
    else:
        return 'Is' + text


if __name__=="__main__":
    print(new_string("Array"))
    print(new_string("IsEmpty"))
    print(new_string("i"))
    print(new_string("Is"))

