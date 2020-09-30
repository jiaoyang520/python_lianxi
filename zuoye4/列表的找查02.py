list01 = ["a", "b", "c", "d", "a"]
li1 = list01
print(li1)
print(id(list01))
print(id(li1))

# index()方法     从左到右找查的第一个指定的元素索引，如果没找到，则报错
print(list01.index("b"))

# count()方法     返回指定的值在列表中的个数
print(list01.count("a"))
