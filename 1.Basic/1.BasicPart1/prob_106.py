'''
Q106. Write a Python program to divide a path by the extension separator. 
'''
import os.path
for path in [ 'test.txt', 'filename', '/home/panditjee/Desktop/PythonExercises/1.Basic/1.BasicPart1/', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))
	