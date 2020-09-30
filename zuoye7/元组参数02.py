def a(*args):
    print(args)



a(1, 2, 3, 4)
tup1 = 1, 3, 5, 7, 9
a(*tup1)
set1 = {1, 3, 6}
a(*set1)
str1 = "hello"
b = a(*str1)


