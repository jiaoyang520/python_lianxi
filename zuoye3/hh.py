# 30 ~ 50 步长为3  相乘

i = 1
num = 0
while i <= 100:
    num += i
    i += 1
print(num)

ii = 30
jj = 1
while ii <= 50:
    jj = jj * ii
    ii += 3

print(jj)

g = 50
while g >= 20:
    if g%3 == 0:
        if g%7 == 0:
            print(g)
    g -= 1