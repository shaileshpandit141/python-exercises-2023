'''
Q24. Write a Python program to test whether a passed letter is a vowel or not.
'''
def is_vowel(leater:str):
    if leater in ('a', 'e', 'i', 'o', 'u'):
        print(f"Leater '{leater}' is vowel.")
        return True
    else:
        print(f"Leater '{leater}' is not vowel.")
        return False

if __name__=="__main__":
    is_vowel('c')
    is_vowel('e')
    is_vowel('y')
