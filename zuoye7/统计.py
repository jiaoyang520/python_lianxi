s = "123456abcdeABCDE__"
shuzi = 0
xiaoxie = 0
daxie = 0
xhx = 0
i = 0
while i < len(s):
    # if s[i] >= "0" and s[i] <= "9":
    if "9" >= s[i] >= "0":
        shuzi += 1
    elif "a" <= s[i] <= "z":
        xiaoxie += 1
    elif "A" <= s[i] <= "Z":
        daxie += 1
    elif s[i] == "_":
        xhx += 1
    i += 1

print(shuzi, xiaoxie, daxie, xhx)