list01 = ["向阳", "陈雪凝", "张杰", "许嵩"]
print(list01)

# 使用索引来实现修改操作
list01[0] = "郭聪明"
print(list01)
list01[3] = "兔子牙"
print(list01)

# reverse()  把列表中的元素翻转一下
list01.reverse()
print(list01)

# sort()方法表示给列表排序
list02 = ["a", "B", "C", "D", "f", "E"]
list02.sort()
print(list02)
list03 = [1, 2, 3, 4, 5]
list03.sort(reverse=True)   # reverse=True降序排序
print(list03)

# 按照指定的规则进行排序
list02.sort(key=str.lower, reverse=True)  # 按照字母的小写进行排序
print(list02)

#
list05 = ["a", "B", "C", "D", "f", "E"]
a = sorted(list05)
print(a)
b = sorted(list05, key=str.lower)
print(b)
c = sorted(list05, reverse=True)
print(c)

