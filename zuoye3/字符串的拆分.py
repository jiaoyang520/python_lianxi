# partition()方法会把字符串拆解为3段,以指定的字符串为分界线
a = "XiangYang"
print(a.partition("a"))
#   以换行符为分割线，进行分割。
b = "my name\n" + "is\n" \
    "xiang yang"
print(b.splitlines())
# 按照指定的内容进行分割,此分割不包括自己的指定的 值
print(a.split("a"))     # maxsplit不写，默认分割所有
print(a.split("a", maxsplit = 1))       # maxsplit分割的次数