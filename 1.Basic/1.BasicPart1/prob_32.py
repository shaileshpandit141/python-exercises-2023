'''
Q32. Write a Python program to find the least common multiple (LCM) of two positive integers.
'''

def print_lcm(num_x:int, num_y:int):
  if num_x > num_y:
      mx = num_x
  else:
      mx = num_y

  while True:
      if mx % num_x == 0 and mx % num_y == 0:
          lcm = mx
          break
      mx += 1
  return lcm


if __name__=="__main__":
    print(print_lcm(4, 6))
    print(print_lcm(15, 17))