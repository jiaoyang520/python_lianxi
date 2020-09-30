tup = (1, 2, 3, 4, 5, 6, 7, 3, 7, 7)
# index()方法返回第一个遇到指定元素的索引，如果没有则报错
print(tup.index(3))
print(tup.index(7))
# count()方法返回指定的元素个数,找不到则返回0
print(tup.count(1))
print(tup.count(7))
print(tup.count(10))