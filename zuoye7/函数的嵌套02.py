def a():
    print("a()")
    def b():
        print("b()")

    b()

a()

def c():
    print("c()")

def d():
    c()
    print("d()")

d()