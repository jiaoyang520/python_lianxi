#
def a(num):
    print(f"传入的参数是{num}")
    if num == 1:
        return
    num = num - 1
    print(num)
    a(num)
    print(num)


a(2)


# 阶乘
def b(num):
    if num == 1:
        return 1
    return num * b(num -1)


print(b(6))