num = int(input("请输入一个数字:"))
if num <= 1:
    print("这不是质数")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print('这不是一个质数')
            break
        i =+ 1
    else:
        print("这是一个质数")