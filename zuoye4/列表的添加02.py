list01 = ["a", "b", "c", "d"]
print(list01)
# append()    在列表末尾加入指定的元素
list01.append("e")
print(list01)
# insert()      将指定的元素插入指定的索引上   注意：负值索引倒序插入   超过索引就会在末尾插入
list01.insert(3, "f")
print(list01)
# extends()方法   将指定的元素拆解依次追加到列表的尾部，不会去重
list01.extend("ggg")
print(list01)

list02 = ["c", "d", "e", "f"]
list03 = list01 + list02
print(list03)