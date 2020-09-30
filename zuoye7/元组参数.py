def a(*args):
    print(args)


str1 = "xiangyang"
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 3, 5, 7, 9)
set1 = {"a", "b", "c", "d", "e"}
dict1 = {"k1": "v1", "k2": "v2"}
a(str1)
a(*list1)
a(*tuple1)
a(*set1)
a(*dict1)