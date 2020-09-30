dict01 = {"name": "向阳", "age": 20}
print(dict01)
# 增添  变量名[key] = value
dict01["height"] = 1.60
print(dict01)
# 修改    变量名[字典中存在的key] = value
dict01["name"] = "黎冠鹏"
print(dict01)
# setDefault(k,v)方法来给字典dict添加新元素
dict01.setdefault("weight", 120)
print(dict01)