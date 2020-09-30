

i = 0
shu = 0
while i < 5:
    num = int(input("请输入位的整数:"))
    # i = num % 10 + i * 10
    # num = num // 10
    # print(num % 10)
    shu = shu + num
    i += 1

print(shu/5)