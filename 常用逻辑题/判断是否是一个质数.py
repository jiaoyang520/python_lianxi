num = int(input("请输入一个数:"))

if num > 2:
    i = 2
    while i < num:
        if num % i == 0:
            print(f"{num}不是质数")
            break
        i += 1
    else:
        print(f"{num}是质数")
else:
    print(f"{num}不是质数")