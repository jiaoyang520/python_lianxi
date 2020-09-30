def a(*args):
    print(args)
    print(type(args))


a(1, 2, 3, 4)
tup1 = 1, 3, 5, 7, 9
a(*tup1)
set1 = {1, 3, 6}
a(*set1)
str1 = "hello"
a(*str1)
a(*str1, *tup1)
dict01 = {"name": 10, "age": 20}
a(*dict01)  # 传一个拆包的字典经过*args参数之后只会把key留下变为元组


# 经过*args参都变为元组的类型tuple


