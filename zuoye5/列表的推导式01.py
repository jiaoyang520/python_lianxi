# 语法1：   变量名 = [表达式 for 变量 in 列表]
# 语法2     变量名 = [表达是 for 变量 in 列表 if 条件]
list01 = [1, 2, 3, 4, 5, 6, 7, 8]
#
for i in list01:
    print(i, end=" ")

print()

new_lis1 = [i for i in list01]
print(new_lis1)
# 平方
new_lis2 = [i * i for i in list01]
print(new_lis2)
# 使用函数


def square(num):
    return num * num


new_lis3 = [square(i) for i in list01]
print(new_lis3)
# 求list11中的奇数，放入新列表中
list11 = [1, 2, 3, 4, 5, 6, 7, 8]
new_list11 = []
for i in list11:
    if i % 2 == 1:
        new_list11.append(i)
print(new_list11)
new_list22 = [i for i in list11 if i % 2 == 1]
print(new_list22)
# 求列表list111中所有大于2的偶数进行平方计算
list111 = [1, 2, 3, 4, 5, 6, 7, 8]
list211 = []
for i in list111:
    if i > 2:
        if i % 2 == 0:
            list211.append(i)
print(list211)
new_list212 = [i for i in list111 if i > 2 if i % 2 == 0]
print(new_list212)
# 将一个嵌套的列表转成一个一维列表
list666 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list777 = []
for i in range(len(list666)):
    for j in range(0, 3):
        list777.append(list666[i][j])
print(list777)
new_list777 = [j for i in list666 for j in i]
print(new_list777)
# 将一个列表li01输出1，4，7和1，5， 9元素
li01 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(li01)):
    print(li01[i][0], end=" ")
print()
new_ls01 = [li01[i][0] for i in range(len(li01))]
print(new_ls01)
for i in range(len(li01)):
    print(li01[i][i], end=" ")
print()
new_ls02 = [li01[i][i] for i in range(len(li01))]
print(new_ls02)

a = [lambda x:x * i for i in range(3)]
print(a[0](2))
print(a[1](2))
print(a[2](2))

