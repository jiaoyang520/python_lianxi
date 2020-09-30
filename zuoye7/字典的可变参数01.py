# **kwargs  字典的可变参数kwargs      需要传的参数也是键值对  key = value
def a(**kwargs):
    print(kwargs)
    for i in kwargs.items():
        print(i, end=" ")


a(name="向阳", age=20, height=1.60)

print()


# 注意  **kwargs 必须放在 *args  后面
def b(*args, **kwargs):
    print(args)
    print(kwargs)


# 注意   传的参需要用*  和  ** 拆包
tup1 = (1, 2, 3)
dict1 = {"name": "向阳", "age": 20}
b(*tup1, **dict1)


# 参数顺序   *args, **kwargs  两个参数必须放在方法的末尾
def c(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


c(10, 77, *tup1, **dict1)
