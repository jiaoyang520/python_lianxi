list01 = ["a", "b", "c", "d", "e"]
print(list01)
list01[0] = "aaa"
print(list01)

# 倒序输出
list01.reverse()
print(list01)

# 按照ascll码表进行排序
list02 = [1, 2, 3, 4]
list02.sort()
print(list02)

list03 = ["A", "B", "a", "b", "f","D"]
list03.sort()
print(list03)
list03.sort(reverse=True)
print(list03)