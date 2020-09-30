dic2 = {
    "001": {"name": "王一博", "age": 18, "address": "泰国"},
    "002": {"name": "贺凯", "age": 18, "address": "宁夏"},
    "003": {"name": "刘强", "age": 18, "address": "汉中"},
    "004": {"name": "王怡欢", "age": 18, "address": "韩国"}
}

#
for i, j in dic2.items():
    print(f"第一层------>>{i}<---->{j}")
    for k, f in j.items():
        print(f"第二层------------------->>>{k}<------>{f}")
    print()



for j in dic2.values():
    if j["address"] == "宁夏":
        j["house"] = 300

print(dic2)

for j in dic2.values():
    for k, f in j.items():
        if k == "address" and f == "宁夏":
            j["house"] = 300

print(dic2)