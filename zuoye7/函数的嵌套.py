# 函数的嵌套必须要在函数内部调用    外部是无法调用
def a():
    print("a()方法")


    def b():
        print("b()方法")

    b()

a()