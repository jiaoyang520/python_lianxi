# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# f = [lst[i][i] for i in range(3)]
# print(f)
# f = [lst[i][len(lst)-i-1] for i in range(len(lst))]
# print(f)
# f = [lst[i][-i-1] for i in range(len(lst))]
# print(f)
# d = [j for i in lst for j in i]
# print(d)


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 1, 5, 9
lis1 = [lst[i][i] for i in range(3)]
# 3, 5, 9
print(lis1)
lis2 = [lst[i][2-i] for i in range(len(lst))]
print(lis2)
lis3 = [lst[i][-i-1] for i in range(len(lst))]
print(lis3)
# 转化一维列表
lis4 = [j for i in lst for j in i]
print(lis4)