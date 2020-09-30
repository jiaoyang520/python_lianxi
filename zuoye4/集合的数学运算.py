
set2 = {1, 2, 3, 4, 5, 6}
set3 = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# 交集&   或者intersection()方法
print(set2 & set3)
print(set2.intersection(set3))
print("--------------------------------")
# 并集|   或者union()方法
print(set2 | set3)
print(set2.union(set3))
print("--------------------------------")
# 差集-   或者difference()方法
print(set2 - set3)
print(set2.difference(set3))
print("---------------------------------")
# 反交集   或者symmetric_difference()方法
print(set2 ^ set3)
print(set2.symmetric_difference(set3))
print("----------------------------------")
# 子集<   或者issubset()方法
print(set2 < set3)
print(set2.issubset(set3))
print("-----------------------------------")
# 超集    或者issuperset()方法
print(set2 > set3)
print(set2.issuperset(set3))
print("-----------------------------------")