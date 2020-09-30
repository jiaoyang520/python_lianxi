tu1 = (1, 3, 6, 7, 9)
for i in tu1:
    print(i)

print("-----------------------------------")
tu2 = ((1, 2), (3, 4), (5, 6))
for i in tu2:
    print(i)
# 拆包
print("-----------------------------------")
for ii, jj in tu2:
    print(ii, jj)
# enumerate()内置函数    该方法遍历并返回每个元素的索引
print("-----------------------------------")
for i in enumerate(tu2):
    print(i)

print("-----------------------------------")
msg = "my name is %s,age is %d"%("xy", 20)
print(msg)

print("-----------------------------------")
def func():
    name = "xiangyang"
    age = 18
    return  name, age


tup7 = func()
print(tup7)
print(type(tup7))