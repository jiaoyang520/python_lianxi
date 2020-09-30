def a(num):
    print(num)
    if num == 1:
        print("-----------------------")
        return "----------------------"
    a(num - 1)
    print(num)

print(a(7))

def b(num):
    if num == 1:
        return num
    return num * b(num - 1)
print(b(7))
