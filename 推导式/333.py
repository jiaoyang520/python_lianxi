def info():
    print("1楼   珠宝")
    print("2楼   服装")
    print("3楼   小吃城")
    print("4楼   海底捞")

floor = int(input("请输入楼层"))
if floor == 1:
    print("万达广场1楼欢迎你")
    info()

if floor == 2:
    print("万达广场2楼欢迎你")
    info()

if floor == 3:
    print("万达广场3楼欢迎你")
    info()

if floor == 4:
    print("万达广场4楼欢迎你")
    info()

def jiafa(a, b):
    c = a + b
    print(c)


jiafa(1, 3)

s = jiafa(3, 4)

def math_(a, b):
    c = a + b
    f = a * b
    g = a / b

print(math_(3, 4))