i = 0
shu = []
while i < 5:
    num = int(input("请输入一个数:"))
    shu.append(num)
    i += 1

print(shu)

for n in range(0, len(shu)):
    for m in range(0, len(shu)):
        if shu[n] > shu[m]:
            buffer = shu[n]
            shu[n] = shu[m]
            shu[m] = buffer


print(shu)
print(f"最大值 {shu[0]},最小值 {shu[-1]}")
