dict01 = {1: "向阳", "age": 20, "height": 1.60, "weight": 120, "k": "v"}
# pop(key)方法使用key找到在这个元素并删除，并返回这个删除的value值
print(dict01.pop("height"))
print(dict01)
# popitem()
print(dict01.popitem())
print(dict01)
# clear()清空字典
dict01.clear()
print(dict01)
# del()方法删除字典
del(dict01)
print(dict01)
