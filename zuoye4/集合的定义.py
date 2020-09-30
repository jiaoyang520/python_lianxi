# 集合中的元素是无序的
# 语法：变量名 = {元素1，元素2，元素n}
# 注意：1.创建一个空集合必须用set(),而不是{}，因为{}是用来创建一个空字典
#      2.集合中的元素必须是不可修改类型
sets = {1, 2, 3, 8, 5, 6, 7}
print(sets)
print(type(sets))
set1 = set([1, 3, 6, 8])
print(set1)
# set()方法中传入一个字符串返回一个拆分开的字符set集合
set2 = set("hello")
print(set2)
# set()方法中传入字典，返回一个只有key的set集合
set3 = set({"name": "向阳", "age": 20})
print(set3)