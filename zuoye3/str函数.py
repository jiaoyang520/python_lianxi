a = "xiangyangxielijiao"

print(a.count('i'))
print(a.find("xie"))
print(a.rfind("li"))
print(a.rfind("i"))
print(a.find("i"))
print(a.index('i'))
print(a.rindex('i'))

print(a.partition("g"))
print(a.partition("yang"))

# maxsplit的值是多少，则按照指定的字符串为分界线分割多少次
print(a.split("i", maxsplit=4))

print(a.replace("i", "e"))
print(a.replace("i", "w", 2))

vv = "    xiangyangxielijiao      "
print(vv.center(50))
print(vv.center(50, "~"))
print(vv.ljust(50, '@'))
print(vv.rjust(50, "%"))
print(vv.zfill(50))
print(vv.strip())
print(vv.lstrip())
print(vv.rstrip())
