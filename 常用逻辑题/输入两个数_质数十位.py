a = int(input("请输入一个数："))
b = int(input("请输入一个数："))

for i in range(a, b+1):
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        if i % 100 // 10 == 3:
            print(i)