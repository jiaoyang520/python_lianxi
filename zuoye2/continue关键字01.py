num = 0
while num < 10:

    if num == 4:
        num += 1
        print("跳出循环")
        continue
    print("当前的num值是%d" % num)
    num += 1

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)