a = " Xiang  Yang  "
# 居中   如果不对称则左短右长       也可以指定内容填充   默认空格填充
print(a.center(30))
print(a.center(30, "~"))
# 左对齐     内容填充到右面      默认空格填充
print(a.ljust(30))
print(a.ljust(30, "@"))
# 右对齐     内容填充到左边      默认填充空格
print(a.rjust(30))
print(a.rjust(30, "%"))
#   将字符串填充到指定长度， 空白地用0在左边填充
print(a.zfill(30))
#   format()函数把字符串的内容传递给字符串中用花括号{}占位的地方
print("hello，my name is {}，today is {} yers".format("向阳", 0))
#   去除空格    去除的内容可以指定
print(a.strip())    # 去除两边空格
print(a.rstrip())   # 去除右边空格
print(a.lstrip())   # 去除左边空格
