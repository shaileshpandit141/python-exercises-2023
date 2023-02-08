'''
Q139. Write a Python program to validate an IP address.
'''
from socket import inet_aton, error
addr = '127.0.0.2561'
try:
    inet_aton(addr)
    print("Valid IP")
except error:
    print("Invalid IP")
