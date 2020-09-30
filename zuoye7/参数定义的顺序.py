# 定义函数时参数的顺序：位置参数， 元组参数，默认参数，字典参数


def fun1(a, *args, name='向阳', **kwargs):
    print(a)
    print(args)
    print(name)
    print(kwargs)


fun1(10, *(1, 2, 3), name="xy", **{"k1": "v1", "k2": "v2"})