'''
Q46. Write a Python program to retrieve the path and name of the file currently being executed.
'''

from os.path import realpath

def retrieve_path_name():
    print("Current File path and name : ",realpath(__file__))

def working_file():
    var = realpath(__file__).split('/') 
    print('Working file name: ', var[(len(var)-1)])

if __name__=="__main__":
    retrieve_path_name()
    working_file()