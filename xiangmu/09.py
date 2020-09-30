num = int(input("请输入一个整数："))
i = 0
j = 0
while i < num:
    j = num % 10 + j * 10
    num = num // 10
print(j)

