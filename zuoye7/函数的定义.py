def a():
    print("a()无参无返回值的方法")


def b(a, b):
    print("b()有参无返回值的方法")
    print(f"返回值是{a}{b}")


def c(a, b):
    print("c()有参有返回值的方法")
    return a + b


a()
b(5, 6)
print(c(7, 8))


def d():
    return 1, 2, 3


print(d())

