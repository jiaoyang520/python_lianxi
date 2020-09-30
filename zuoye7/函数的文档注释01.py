# 函数的文档注释
def a():
    '''该方法是a()'''
    print("a()方法")


def b():
    """ 该方法是b()"""
    print("b()方法")

# 使用  方法名·__doc__  内置方法就可以打印出该方法的文档注释
a()
b()
print(a.__doc__)
print(b.__doc__)