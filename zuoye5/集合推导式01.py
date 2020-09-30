set01 = {1, 2, 3, 3, 4, 5, 6, 6, 7, 2}
print(set01)
for i in set01:
    print(i, end=" ")
print()
set02 = {i for i in set01}
print(set02)

list01 = [1, 2, 3, 3, 4, 5, 6, 6, 7, 2]
set03 = {i for i in list01}
print(set03)

# 计算列表中list01中每个值的平方，并去重
set07 = {i * i for i in list01}
set08 = {i * i for i in list01}
print(set07)
print(set08)

set66 = {"xi", "an", "g", "ya", "an", "g"}
print(set66)