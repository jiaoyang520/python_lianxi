dict01 = {"name": "向阳", "age": 20, "height": 120}
# in 判断指定的键是否在字典中
if "name" in dict01:
    print("存在")
else:
    print("不存在")

# not in 判断指定的键不存在
if "na" not in dict01:
    print("不存在")
else:
    print("存在")

print("----------------------------------------")
# 遍历字典
for key in dict01:
    print(key)
print("----------------------------------------")
for key in dict01.keys():
    print(key)
print("----------------------------------------")
for value in dict01.values():
    print(value)
# items()返回字典键值对以元组的格式
print("----------------------------------------")
for it in dict01.items():
    print(it)
# items()返回字典键值对以元组的格式
print("----------------------------------------")
for key, value in dict01.items():
    print(f"{key}------------------->>{value}")
