i = 0
while i < 10:
    print("————————————————++++++++++%d"%i)
    i += 1

i = 1
num = 0
while i <= 100:
    num += i
    i += 1

print(f"1~100的和是: {num}")


ii = 1
jj = 1
while ii <= 7:
    jj = 1
    while jj <= ii:
        print(f"*", end=" ")
        jj += 1
    print()
    ii += 1


# jj = 1
# while jj <= 7:
#     print("*")
#     jj += 1