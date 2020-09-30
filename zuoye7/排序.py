max = 0
min = 0
i = 0
while i < 5:
    num = int(input("请输入一个数字: "))
    if i == 0:
        max = num
        min = num
    else:
        if num > max:
            max = num
        elif num < min:
            min = num
    i += 1

print(max, min)

max1 = 0
min1 = 0
i1 = 0
while i1 < 5:
    num1 = int(input("请输入一个数字: "))
    if i1 == 0:
        max1 = num1
        min1 = num1
    else:
        if num1 > max1:
            max1 = num1
        elif num1 < min1:
            min1 = num1
    i1 += 1
print(max1, min1)

max2 = 0
min2 = 0
i2 = 0
while i2 < 5:
    num2 = int(input("请输入一个数字: "))
    if i2 == 0:
        max2 = num2
        min2 = num2
    else:
        if num2 > max2:
            max2 = num2
        elif num2 < min2:
            min2 = num2
    i2 += 1
print(max2, min2)

max3 = 0
min3 = 0
i3 = 0
while i3 < 5:
    num3 = int(input("请输入一个数字："))
    if i3 == 0:
        max3 = num3
        min3 = num3
    else:
        if num3 > max3:
            max3 = num3
        if num3 < min3:
            min3 = num3
    i3 += 1
print(max3, min3)

max4 = 0
min4 = 0
i4 = 0
while i4 < 5:
    num4 = int(input("请输入一个数字:"))
    if i4 == 0:
        max4 = num4
        min4 = num4
    else:
        if num4 > max4:
            max4 = num4
            min4 = num4
        else:
            if num4 > max4:
                max4 = num4
                min4 = num4
            elif num4 < min4:
                min4 = num4
    i4 += 1
print(max4, min4)