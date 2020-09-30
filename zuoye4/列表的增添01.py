# append()方法表示在列表的末尾添加指定的元素
list01 = ["向阳", "陈雪凝", "邓紫棋", "许嵩", "郭聪明"]
print(list01)
list01.append("鞠婧祎")
list01.append("向阳")
print(list01)

# extend()方法会把字符串中的内容拆分开，然后在列表末尾依次添加
list01.extend("陈雪凝")
list01.extend("123456")
print(list01)


# insert()方法将指定的元素插入到对应的索引的位置，注意:1.负值是倒着插入元素的，2.超过索引值则在末尾添加元素
list01.insert(10, "张杰")
list01.insert(-3, "李荣浩")
print(list01)

# + 使用 + 拼接list列表    注意:使用 + 拼接列表时   与变量名的前后顺序有关
li = ["hello", "word!"]
lis = list01 + li
lis1 = li + list01
print(f"---->> {lis}")
print(f"------->>>{lis1}")