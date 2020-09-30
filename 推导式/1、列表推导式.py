# -*- coding: utf-8 -*-


#  [0,1,2,3,4,5,6,7,8,9]
a = [i for i in range(10)]
# print(a)

# 1-100只输出奇数

b = [i for i in range(1, 100, 2)]
# print(b)

c = [i for i in range(2, 100, 2)]
# print(c)

# 输出200-500之间能被5或者7整除的数

d = [i for i in range(200, 501) if i % 5 == 0 or i % 7 == 0]
# print(d)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1,5,9]
# for i in lst:
#     print(i)
i = 0
while i < len(lst):
    j = 0
    while j < len(lst[i]):
        if j == i:
            print(lst[i][j])
        j += 1
    i += 1

f = [lst[i][i] for i in range(len(lst))]
print(f)

# [3,5,7]

"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

"""

# 用推导式生成   [[1,2,3],[4,5,6],[7,8,9]]
# 提示：用两个for循环

# 第一种
lst = [] # 嵌套列表
new_lst = [] # 最终生成大列表
count = 0 # 计数
for i in range(1, 10):
    lst.append(i)
    count += 1
    if count == 3:# 当嵌套列表添加三个元素后，添加到新列表里面，嵌套列表置空，计数器置空
        new_lst.append(lst)
        count = 0
        lst=[]
print("new_lst",new_lst)


lst = [i for i in range(1,10)]
print("lst",lst)

new_lst = [lst[j:j+3] for j in range(0,len(lst),3)]
print("new_lst",new_lst)

print("================================================")
new_lst = [[i for i in range(1,10)][j:j+3] for j in range(0,len([i for i in range(1,10)]),3)]
print(new_lst)
# 第二种

# new_lst = []

for i in range(3):
    lst = []
    for j in range(3):# 计数器
        lst.append(3*i+j+1)
    new_lst.append(lst)
# print("new_lst",new_lst)
f = [[3*i+j+1 for j in range(3)]for i in range(3)]
# print(f)

