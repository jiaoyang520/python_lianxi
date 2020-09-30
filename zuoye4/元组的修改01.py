# 元组是不可修改的数据类型,所以其中的元素不能被修改
tup1 = ("程鹏大儿子", "陈鹏儿子")
# tup1[0] = "chen"     # TypeError: 'tuple' object does not support item assignment  类型错误:“tuple”对象不支持项分配

# 如果元组中的元素是一个可变类型的列表，南无其嵌套就可以被改变
tup = ("账号", "密码", ["向阳", "陈鹏"])
tup[2][0] = "hello"
tup[2].append("word")
print(tup)


