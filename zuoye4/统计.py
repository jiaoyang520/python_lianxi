s = "123abcABCDE_"
i = 0
shuzi = 0
daxie = 0
xiaoxie = 0
fuhao = 0
while i < len(s):
    if 48 <= ord(s[i]) <= 57:
        shuzi += 1
    elif 65 <= ord(s[i]) <= 90:
        daxie += 1
    elif 97 <= ord(s[i]) <= 122:
        xiaoxie += 1
    else:
        fuhao += 1
    i += 1
print(shuzi)
print(daxie)
print(xiaoxie)
print(fuhao)
