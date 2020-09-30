dic = {"name": "肖战", "age": 30, "sex": "女", "address": "泰国"}
dic["sex"] = "男"
print(dic)
dic["age"] = 48
print(dic)
dic.pop("name")
print(dic)
del dic["age"]
print(dic)
dic["name"] = "何凯"
print(dic)
dic["sex"] = "女"
print(dic)

dic1 = dict(name="王一博", age=60, sex="女", address="东莞")
print(dic1)
print(dic1["name"])
print(dic1.get("name"))
print(dic1.get("sex", "男"))
print(dic1.get("Hair", "黑色"))
print(dic1)

print(dic1.keys())
for i in dic1.keys():
    print(i)

print(dic1.values())
for i in dic1.values():
    print(i)

print(dic1.items())
for i in dic1.items():
    print(i)

for k, v in dic1.items():
    print(k, v)

print()

dic2 = {
    "001": {"name": "王一博", "age": 18, "address": "泰国"},
    "002": {"name": "贺凯", "age": 18, "address": "宁夏"},
    "003": {"name": "刘强", "age": 18, "address": "汉中"},
    "004": {"name": "王怡欢", "age": 18, "address": "韩国"}
}

for d in dic2.values():
    print(d)

print("----------------------------------------------------")

for i in dic2.values():
    print(i)
    for j in i.items():
        print(j)

# 当 address = "宁夏" 的时候，给添加 "house": "300平"

for i in dic2.values():
    if i["address"] == "宁夏":
        i["house"] = "300平"
print(dic2)

for i in dic2.values():
    print(i)

print("-------------------------------------------------")

d = {"name": "贺凯", "age": 18, "address": "宁夏"}
# 取出宁夏
nx = d.get("address")
nx1 = d["address"]
print(nx, nx1)
# d.clear()
# print(d)
d.popitem()
print(d)
d.pop("age")
print(d)
d.update({"age": 20})
print(d)
d["age"] = 30
print(d)