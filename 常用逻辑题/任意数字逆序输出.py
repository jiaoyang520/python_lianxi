num = int(input("请输入一个数："))
i = 0
while num > 0:
    i = num % 10 + i * 10
    num = num // 10

print(i)