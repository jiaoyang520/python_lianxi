# range()函数

for i in range(5):
    print(i)
print("________________________________")
for i in range(1, 5):     # 不包含结尾的数
    print(i)

print("___________________________________")
for i in range(1, 5, 2):        # 步长为二    不包含结尾的数
    print(i)

print("__________________________________")
for i in range(3):
    print("外出循环：", i)
    for j in range(3):
        print(j, "_____________________>>")