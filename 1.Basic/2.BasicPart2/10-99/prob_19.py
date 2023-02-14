"""Q19. Write a Python program that finds the value of n when n degrees of number 2 are written sequentially on a
line without spaces between them."""


def ndegrees(num):
    ans = True
    n, tempn, i = 2, 2, 2
    while ans:
        if str(tempn) in num:
            i += 1
            tempn = pow(n, i)
        else:
            ans = False
    return i - 1


print(ndegrees("2481632"))
print(ndegrees("248163264"))
