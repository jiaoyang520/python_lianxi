# 字典的推导式也是列表推导式思想的延续，语法相似。
# 字典的推导式：
#           变量名 = {表达式 for 变量key，变量value in 可迭代对象 ......}
#           变量名 = {表达式 for 变量key，变量value in 可迭代对象 if 条件}

# 题目1：使用字典推导式创建一个新的字典
# 把字典dict1的元素
dict1 = {"name": "xy", "age": 20, "height": 1.61}

# 普通方法：
dict2 = {}
for k, v in dict1.items():
    dict2[k] = v
print(dict2)

# 推导式：
dict3 = {k: v for k, v in dict1.items()}
print(dict3)