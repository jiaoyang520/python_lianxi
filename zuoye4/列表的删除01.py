list01 = ["向阳", "陈雪凝", "邓紫棋", "许嵩", "郭聪明", "兔子牙", "hello", "word", "!"]
print(list01)

# pop()方法返回并删除指定索引上的数据
list01.pop()
print(list01)
list01.pop(7)
print(list01)

# remove()方法从左往右删除一个指定的元素
list01.remove("hello")
print(list01)

# clear()方法清除列表中的数据
list01.clear()
print(list01)

# del()方法   删除整个列表
del(list01)
# del list01
print(list01)   # NameError: name 'list01' is not defined 报错未定义

