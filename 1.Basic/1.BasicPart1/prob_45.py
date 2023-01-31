'''
Q45. Write a Python program that calls an external command. 
'''

from os import system
from subprocess import call
import psutil

def run_command(command_name:str):
    system(command_name)

def call_command(command_list:list):            # call function is run only one string/command. otherwise run multiple string/command by using list format.
    call(command_list)

def cpu_core_count():
    print(psutil.cpu_count())

if __name__=="__main__":
    print("system command: ")
    command = 'pwd'
    run_command(command)

    print("coll command: ")
    command_l = ["ls", "-l"]
    call_command(command_l)
    
    print( "number of cpu core: ")
    cpu_core_count()
    