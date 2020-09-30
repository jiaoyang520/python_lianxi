# 字符串的找查
a = "Xiang Yang"
# 通过指定的字符查对应的索引，找不到返回-1
print(a.find("a"))  # 从左开始查找
print(a.rfind("n"))     # 从右开始查找
print(a.find("z"))
# 通过指定的字符查对应的索引 找不到则报错
print(a.index("i"))     # 从左开始找查        找不到则报错
# print(a.index("II"))
print("sfjsdilfk", a.rindex("g"))        # 从右开始找查
# 计数自己定义的字符在字符串中的个数
print(a.count("a"))