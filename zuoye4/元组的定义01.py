# 元组是不可修改的
# 有序
# 多个元素的元组语法:变量名 = (元素1, 元素2, 元素n)
tup = ("my", "name", "is", "xiangyang")
print(tup)
print(type(tup))
print(tup[0])
for i in range(len(tup)):
    print(tup[i])


tup1 = (1, 2)
tup2 = (3, 7)
tup3 = tup1 + tup2
print(tup3)

# 单个元素的元组语法:变量名 = (元素,)
tup5 = ("xiangyang",)
tup6 = tup5 * 7
print(tup6)

# 多维元组
tup7 = ((1, 2, 3, 4, 5), (7, 8), (9, 0))
print(tup7)
print(tup7[1][0])

# 多个变量接收元组中的值
t1, t2, t3 = ("my", 7, False)
print(t1, t2, t3)
t11, t22, t33 = (1, 2), (3, 4), (5, 6)
print(t11, t22, t33)

# 序列解包
tu1, *tu2 = (1, 2, 3, 4, 5, 6)
print(tu1)
print(tu2)

*tu3, tu4 = (1, 2, 3, 4, 5, 6)
print(tu3)
print(tu4)

