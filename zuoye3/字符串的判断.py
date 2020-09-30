
# isalnum()方法判断是否完全由字母或数字组成
a = "xiangyang"
print(a.isalnum())
b = "x113"
print(b.isalnum())
c = "xy123321"
print(c.isalnum())
d = "向阳"
print(d.isalnum())
#   isalpha()判断字符串是否完全由字符串组成
e = "xiangyang"
print(e.isalpha())
f = "123321"
print(f.isalpha())
#   isdigit()判断字符串是否完全右数字组成
j = "167951"
print(j.isdigit())
print(e.isdigit())
# isupper()判断字符串中的字母是否完全是大写
h = "XIANG YANG"
print(h.isupper())
# islower()判断字符串中的字母是否完全是小写
print(e.islower())
# istitle()判断首字母是否大写（标题）
ss = "Http"
print(ss.istitle())
# isspace()判断字符串是否完全由空格组成
aa = "    "
print(aa.isspace())
# startswith()判断字符串是否以指定的字符开头
bb = "xiangyang"
print(bb.startswith("x"))
#   endswith()判断字符串是否以指定的字符结尾
print(bb.endswith("g"))
#    split()分割字符串
print(bb.split("a", 2))