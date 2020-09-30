dict01 = {"name": "向阳", "age": 20, "height": 1.60, "weight": 120}
# 语法：变量名[key] = value    key存在就覆盖，不存在就新增
dict01["name"] = "陈鹏儿子"
print(dict01)
dict01["hello"] = "word"
print(dict01)

# update()方法   传递一个字典  在新的字典中key存在就覆盖，不存在就新增
dict02 = {"name": "向阳", "age": 20, "hei": 1.60, "wei": 120, "name": "陈鹏大儿子"}
dict01.update(dict02)
print(dict01)

