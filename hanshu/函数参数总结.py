# 函数参数总结：
# 定义函数时参数的顺序：位置参数，元组参数， 默认参数，字典参数


def a(b, *args, c=777, **kwargs):
    print(b, args, c, kwargs)


a(10, *(1, 3, 5, 7), name="jy")
