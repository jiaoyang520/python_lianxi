# *具有打散序列的功能   可以打散  tuple  list   set   dict
def a(a, b, c):
    print(a, b, c)


tup01 = (1, 2, 3)
a(*tup01)
print(*tup01)
print("-------------------------------------")
print(*[1, 3, 5])
print(*(1, 3, 5))
print(*{1, 3, 5})
print(*{"a": 1, "b": 3, "c": 5})
print(*"135")