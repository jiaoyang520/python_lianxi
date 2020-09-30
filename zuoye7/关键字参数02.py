def a(a, b):
    return a + b


print(a(b=99, a=77))
# 注意：关键字参数必须在位置参数后面
print(a(99, b=77))