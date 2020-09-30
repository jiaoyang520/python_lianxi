# 将字符串转为元组,会把字符串拆成字符，依次添加到元组中去
s = "123231"
tup1 = tuple(s)
print(tup1)     # ('1', '2', '3', '2', '3', '1')
# 将列表转为元组
li = [1, 2, 3, 4, 5, 6, 7]
li1 = ["11", "22", "33"]
tup2 = tuple(li)
tup3 = tuple(li1)
print(tup2)
print(tup3)
# 将元组转化为元组  引用的是同一个内存地址
tu4 = (1, 2, 3, 4)
tu5 = tuple(tu4)
print(tu5)
print(id(tu4))
print(id(tu5))