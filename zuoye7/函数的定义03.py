def a():
    print("无参,无返回")


def b(a, b):
    print("有参,无返回")


def c(a, b):
    print("有参,有返回")
    return a + b


a()
b(1, 2)
c(7, 9)