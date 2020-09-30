a = int(True)
print(type(a), a)
b = int(False)
print(type(b), b)

c = int(10.9)
print(type(c), c)

d = int("10")
print(type(d), d)

e = float(10)
print(type(e), e)
bb = float(True)
print(type(bb), bb)
cc = float("10")
print(type(cc), cc)

aaa = str(True)
print(type(aaa), aaa)
bbb = str(10)
print(type(bbb), bbb)
ccc = str(10.34)
print(type(ccc), ccc)

# chr()是按照utf-8编码表，将10进制的数字转换成对应的字符
h = chr(25105)
print(type(h), h)

