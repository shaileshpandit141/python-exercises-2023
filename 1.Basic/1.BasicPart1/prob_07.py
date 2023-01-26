'''
Q7. Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
Sample filename : abc.java
Output : java
'''
def Print_file_extension(filename):
    var = filename.split(".")
    # print(var)
    print("The extension of the file is:", var[-1])

if __name__=="__main__":
    filenameis = 'main.py'
    Print_file_extension(filenameis)