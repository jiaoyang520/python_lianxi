num = int(input("请输入一个整数:"))
i = 2
while num > i:
    if num % i == 0:
        print(f"{num}不是质数")
        break
    i += 1
else:
    print(f"{num}是质数")