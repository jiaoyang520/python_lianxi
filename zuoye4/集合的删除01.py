set1 = {"向阳", "hello", "word"}
# pop()方法随机删除一个,并返回删除删除的值
print(set1.pop())
print(set1)
# remove()方法删除一个指定的元素
set2 = {"向阳", "hello", "word"}
set2.remove("hello")
print(set2)
# clear()方法方法清空集合
set3 = {"向阳", "hello", "word"}
set3.clear()
print(set3)
# del()或者del  删除这个集合
set4 = {"向阳", "hello", "word"}
del(set4)
print(set4)     #NameError: name 'set4' is not defined    名称错误:未定义名称“set4”