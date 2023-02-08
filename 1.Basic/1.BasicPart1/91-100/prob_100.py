'''
Q100. Write a Python program to get the name of the host on which the routine is running.
'''
from socket import gethostname

host_name = gethostname()
print("Host name:", host_name)
