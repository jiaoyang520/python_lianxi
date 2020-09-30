dict01 = {"name": "向阳", "age": "20", "height": 1.60}
# keys()放回字典中所有key的 列表
print(dict01.keys())
# values()返回字典中所有的value的  列表
print(dict01.values())
# get()以键取值，如果指定的键不存在，默认返回None，可以指定返回的内容
print(dict01.get("age"))
print(dict01.get("weight"))
print(dict01.get("weight", "元素存在"))
# update()以字典的格式更新指定的内容，如果key不存在，则新建，如果存在则就覆盖
dic1 = {"age": 19, "weight": 120}
dict01.update(dic1)
print(dict01)
# items()  返回的字典以元组形式的格式返回
print(dict01.items())
# len()  返回元素的个数
print(len(dict01))