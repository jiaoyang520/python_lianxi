# 语法：无参，无返回值的函数定义
# def 函数名(形参):
#    代码块
#    实参


def a():
    print("a()方法无参，无返回值")


def b(a, b):
    print(f"b()方法有参，无返回值,参数是{a, b}")

# 位置参数赋值是需要按照顺序赋值
def c(a, b):
    print("c()方法有参，有返回值")
    return a + b


a()
b(1, 2)
print(c(7, 7))


def d():
    s = 3.14 * 3 ** 2
    print(s)


d()
# 函数调用的本质是函数名对应的内存地址
print(id(a))
print(id(b))
print(id(c))
print(id(d))


def e():
    return i + 1


i = 5
h = e
j = e
print(h())
i = 7
print(h())
print(j())


def aa(r):
    s1 = 3.14 * r ** 2
    return s1


print(aa(33))
print(aa(77))


# 返回多个值就是返回tuple元组    语法上返回一个tuple可以省略括号
def aaa(r):
    s11 = 3.14 * r ** 2
    ccc = 2 * 3.14 * r
    return s11, ccc


print(aaa(222))
print(aaa(777))


q = aaa(77)
print(q)

ss, cc = q
print(ss)
print(cc)


# 形参使用 变量名 = 值  的情况下可以不按照顺序写   此形参赋值的方式叫  关键字参数
def sas(num1, num2):
    num3 = num1 + num2
    print(num3)


sas(num2=100, num1=99)


# 关键字参数和位置参数同时使用时，关键字参数必须在位置参数后面定义
def aaaaa(num1, num2):
    print(num1, num2)


aaaaa(10, num2=20)
aaaaa(20, num2=100)