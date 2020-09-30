list1 = ["向阳", "黎冠鹏", "陈鹏", "陈雪凝", "hello word!"]
print(list1)

#   通过列表的索引获取列表中的对应元素
li1 = list1[0]
li2 = list1[4]
print(li1, li2)

#   通过for循环遍历列表
i = 0
for li in list1:
    print("第{}个元素是: {}".format(i, li), end="\n")
    i += 1

