'''
Q38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2 = 49
'''
def solve_Q(num1:int, num2:int):
    print(f"({num1} + {num2})^ 2 =",(num1 + num2) **2)

if __name__=="__main__":
    x = 4
    y = 3
    solve_Q(x, y)
    