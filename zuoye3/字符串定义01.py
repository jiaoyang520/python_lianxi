name = '向阳'
addr = "陕西汉中"
hobby = """陕西汉中市南郑县大河坎"""

name = 'My Name is Mike'
a = name[0]
print(a)
a1 = name[-1]
print(a1)

# 步长
s = 'hello world'
s1 = s[0:8:1]
print(s1)
s2 = s[0:8:2]
print(s2)
s3 = s[0:8]     # 步长默认为1
print(s3)
s6 = s[1:8:2]
print("s6--->>>%s"%s6)

# 结束
j = 'hello world'
j1 = s[0:8]
print(j1)

j2 = s[0:]
print(j2)

# 起始
i = 'hello world'
i1 = i[0:6]
print(i1)
i2 = i[:8]
print(i2)

# 综合练习
h = 'hello world'
h1 = h[:]
print(h1)
h2 = h[::]
print(h2)
h3 = h[::2]
print(h3)
h4 = h[4::2]
print(h4)

# 负值练习
ss = 'xiangyang'
ss1 = ss[0:8:-1] # 方向相反  所以不能截取
print(ss1)
ss2 = ss[8:0:-1]
print(ss2)
ss3 = ss[::-1]
print(ss3)

# 其实索引和结束索引为负值
aa = 'xiang yang'
aa1 = aa[-8:5]
print(aa1)
aa2 = aa[0:-8]
print(aa2)
aa3 = aa[-1:-8:-2]
print(aa3)

for s in 'tom':
    print(s)


for s in 'tom':
    print(s)
else:
    print('程序执行完了')

