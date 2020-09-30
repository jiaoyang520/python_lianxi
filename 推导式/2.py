# 集合的推导式与列表的非常相似，唯一区别在于用{}代替[]。而且set集合还有去重的功能

# 集合推导式语法：
# 变量名={表达式 for 变量 in 可迭代对象}   或者   变量名 = {表达式 for 变量 in 可迭代对象 for 变量 in  ......}
# 变量名 = {表达式 for 变量 in 可迭代对象 if 条件}

# 题目1:使用其他序列创建一个新的集合序列
# 集合
set1 = {1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7}
set2 = {i for i in set1}
print(set2)

# 字符串
str1 = "42314124312"
set3 = {i for i in str1}
print(set3)

# 元组
tup1 = (1, 3, 4, 4, 5, 6, 6, 7)
set4 = {i for i in tup1}
print(set4)

# 列表
list1 = [0, 1, 2, 3, 4, 5, 6, 7]
set5 = {i for i in list1}
print(set5)

# 字典
dict01 = {"k1": "v1", "k2": "v2", "k3": "v3"}
set6 = {i for i in dict01}
print(set6)
# 注意：使用推导式把字典转为新的集合推导式，只有字典的key被转入