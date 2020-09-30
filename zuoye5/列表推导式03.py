list01 = {1, 2, 3, 4, 5, 6, 7, 8}
new_01 = [i for i in list01]
print(new_01)
new_02 = [i * i for i in list01]
print(new_02)
new_03 = [i for i in list01 if i % 2 == 1]
print(new_03)
new_04 = [i for i in list01 if i > 2 if i % 2 == 0]
print(new_04)

list11 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_li01 = [j for i in list11 for j in i]
print(new_li01)
new_li02 = [list11[i][0] for i in range(len(list11))]
print(new_li02)
new_li03 = [list11[i][i] for i in range(len(list11))]
print(new_li03)