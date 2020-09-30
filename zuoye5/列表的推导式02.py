list01 = {1, 2, 3, 4, 5, 6, 7, 8}
print(list01)
new_list01 = [i for i in list01]
print(new_list01)
new_list02 = [i * i for i in list01]
print(new_list02)
new_list03 = [i for i in list01 if i % 2 == 1]
print(new_list03)
new_list04 = [i for i in list01 if i > 2 if i % 2 == 0]
print(new_list04)

list11 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list12 = [j for i in list11 for j in i]
print(new_list12)
new_list13 = [list11[i][0] for i in range(len(list11))]
print(new_list13)
new_list14 = [list11[i][i] for i in range(len(list11))]
print(new_list14)