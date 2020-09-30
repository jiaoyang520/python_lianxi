#   元组的可变参数  *args   其中args可以随意命名，但一般都已args命名
def tuple1(*args):
    print(args)
    for i in args:
        print(i, end=" ")


tuple1(1, 3, 5, 6, 7, 8)
