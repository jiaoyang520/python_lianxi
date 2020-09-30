def pr(num):
    print(num)
    if num == 1:
        return num
    pr(num-1)
    print("-------------->>", num)


pr(7)


def a(num):
    if num == 1:
        return num
    return num * a(num - 1)


print(a(7))