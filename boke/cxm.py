s = "1234abcABCDE_"
shuzi  = 0
zimu = 0
xhx = 0
i = 0
while i < len(s):
    if s[i] >= "0" and s[i] <= "9":
        shuzi += 1
    elif (s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z"):
        zimu += 1
    elif s[i] == "_":
        xhx += 1
    i += 1


print(shuzi)
print(zimu)
print(xhx)

max = 0
min = 0
j = 0
while j < 5:
    num = int(input("请输入一个数:"))
    if j == 0:
        max = num
        min = num
    else:
        if num > max:
            max = num
        elif num < min:
            min = num
    j += 1

print(max)
print(min)