# 使用   *变量名    来接收多个元素，并且和位置无关
    # 没有使用 * 的变量  返回的是一个字符串类型的
    # 使用 * 的变量  返回一个list列表

list01, *list02 = ["向阳", "黎冠鹏", "陈鹏", "hello word!"]
print(list01)       # 向阳
print(list02)       # ['黎冠鹏', '陈鹏', 'hello word!']
#
*list1, list2 = ["my", "name", "is", "xiangyang"]
print(list1)        # ['my', 'name', 'is']
print(list2)        # xiangyang

#
s1, *s2 = "hello"
print(s1)       # h
print(s2)       # ['e', 'l', 'l', 'o']

