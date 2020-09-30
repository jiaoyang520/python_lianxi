# 字典参数 **kwargs  传参数时只能传键值对
def a(**kwargs):
    print(kwargs)


a(a=10, b=20, c=30)
dict01 = {"name": "xy", "age": 20}
a(dict01)