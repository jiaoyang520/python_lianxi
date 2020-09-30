# 查看字符串中的函数
aa = "xiang yang"
b = dir(aa)
j = 1
for i in b:
    print(f"第{j}函数是: {i}", end="\n")
    j += 1
# help()查看帮助文档
print(help(str))

