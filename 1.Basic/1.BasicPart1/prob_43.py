'''
Q43. Write a Python program to get OS name, platform and release information.
'''

import os, sys, platform, sysconfig

print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())