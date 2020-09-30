# 变量的引用
a = 7 + 7
b = a
c = b
b = 7777

print(a)
print(b)
print(c)

print(f"{id(a)}")
print(id(b))
print(id(c))

age = 18
print(type(age))
gender = False
print(type(gender))
height = 1.78
print(type(height))

a = 10 + 3
print(a)
num1 = 2
num2 = 3
num3 = num1 + num2
print(num3)

num4 = num1*num2
print(num4)

b1 = True
b2 = False
b3 = b1 + b2
print(b3)

weight = 4
price = 3
money = weight + price
print(money)
money = money - 2
print(money)