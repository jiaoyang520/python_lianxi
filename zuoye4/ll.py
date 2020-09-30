a = [123, 4567, 12, 3456]
i = 0
while i < len(a):
    b = 0
    while a[i] > 0:
        b = b * 10 + a[i] % 10
        print(b)
        print(a[i] // 10)
        a[i] = a[i] // 10
    a[i] = b
    i += 1
print(a)