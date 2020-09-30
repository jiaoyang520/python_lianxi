s = "1234abcABCDE_"
shuzi = 0
zimu = 0
xhx = 0
i = 0
while i < len(s):
    if s[i] >= "0" and s[i] <= "9":
        shuzi += 1
    elif (s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z"):
        zimu += 1
    elif s[i] == "_":
        xhx += 1
    i += 1
print(shuzi, zimu, xhx)

s1 = "1234abcABCDE_"
shuzi1 = 0
zimu1 = 0
xhx1 = 0
i1 = 0
while i1 <len(s1):
    if s1[i1] >= "0" and s1[i1] <= "9":
        shuzi1 += 1
    elif (s1[i1] >= "a" and s1[i1] <= "z") or (s1[i1] >= "A" and s1[i1] <= "Z"):
        zimu1 += 1
    elif (s1[i1] == "_"):
        xhx1 += 1
    i1 += 1
print(shuzi1, zimu1, xhx1)

s2 = "1234abcABCDE_"
shuzi2 = 0
zimu2 = 0
xhx2 = 0
i2 = 0
while i2 < len(s2):
    if s2[i2] >= "0" and s2[i2] <= "9":
        shuzi2 += 1
    elif (s2[i2] >= "a" and s2[i2] <= "z") or (s2[i2] >= "A" and s2[i2] <= "Z"):
        zimu2 += 1
    elif (s2[i2] == "_"):
        xhx2 += 1
    i2 += 1
print(shuzi2, zimu2, xhx2)

s3 = "1234abcABCDE_"
shuzi3 = 0
zimu3 = 0
xhx3 = 0
i3 = 0
while i3 < len(s3):
    if s3[i3] >= "0" and s3[i3] <= "9":
        shuzi3 += 1
    elif (s3[i3] >= "a" and s3[i3] <= "z") or (s3[i3] >= "A" and s3[i3] <= "Z"):
        zimu3 += 1
    elif (s3[i3] == "_"):
        xhx3 += 1
    i3 += 1
print(shuzi3, zimu3, xhx3)

s4 = "1234abcABCDE_"
shuzi4 = 0
zimu4 = 0
xhx4 = 0
i4 = 0
while i4 < len(s4):
    if s4[i4] >= "0" and s4[i4] <= "9":
        shuzi4 += 1
    elif (s4[i4] >= "a" and s4[i4] <= "z") or (s4[i4] >= "A" and s4[i4] <= "Z"):
        zimu4 += 1
    elif (s4[i4] == "_"):
        xhx4 += 1
    i4 += 1
print(shuzi4, zimu4, xhx4)
