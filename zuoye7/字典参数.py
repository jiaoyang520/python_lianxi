# 以key=value的形式传参
def a(**kwargs):
    print(kwargs)


a(k1="v1", k2="v2")


def b(name="zs", age=10):
    print(name, age)


dict1 = {"name": "xy", "age": 20}
b(**dict1)