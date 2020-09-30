num = int(input("请输入一个数："))
j = 2

if num >= 2:
    while j < num:
        if (num % j) == 0:
            print("不是质数")
            break
        j += 1
    else:
        print("是质数")
else:
    print("不是质数")

