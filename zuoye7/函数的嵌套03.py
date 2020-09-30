def a():
    print("a()")
    def b():
        print("b()")
    b()


a()

def d():
    print("d()")

def e():
    d()
    print("e()")


e()