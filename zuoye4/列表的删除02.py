list01 = ["a", "b", "c", "d", "f", "g"]
# pop()方法   删除并返回指定索引的数据，默认删除索引为-1的元素
print(list01.pop())
print(list01)
print(list01.pop(0))
print(list01)

# remove()方法     删除从左往右一个指定的元素
list01.remove("f")
print(list01)

# clear()清空列表
list01.clear()
print(list01)

# del或del()删除整个列表
#del list01
del(list01)
print(list01)