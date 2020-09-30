# 字符串转十进制
s = "az"

# 1.使用字符串转ASCLL表的十进制
for i in s:
    print(ord(i))
# 2.使用ASCLL表的十进制转字符串
print(chr(97))
print(chr(122))


# hex(n) 转化为16进制,以0x开头
print(hex(100))
# oct(n) 转换为8进制,以0o开头
print(oct(100))
# bin(n) 转换为2进制
print(bin(100))
# int(n) 转换为10进制
print(int(100))