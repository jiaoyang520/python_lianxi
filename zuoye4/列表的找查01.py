list01 = [1, 2, 3, 4, 5, 2, 1, 2]
# 使用下标找查
li1 = list01[0]
print(li1)

#   conunt()方法返回元素在列表中的个数
print(list01.count(2))
print(list01.count(1))

# index()方法从左往右找查第一个被指定的元素索引，没找到则报错
print(list01.index(2))
print(list01.index(5))