# 优先级  not > and > or
    # and 且  短路逻辑：一假则假    第一个条件是假后面则不再执行
    # or  或  短路逻辑：一真则真    第一个条件是真后面则不再执行
# and运算符  只要有一个值为0，则结果为0，否则结果为最后一个非0数字
a = 0
b = 1
c = 2
d = 3
f = 0

b1  = a and b and c
print(b1)
print(b and a)
print(d and b)
print(b and d)

# or运算符 只有所有值为0，那么结果才为0，否则结果为第一个非0数字

print(a or f)
print(a or b)
print(d or b)