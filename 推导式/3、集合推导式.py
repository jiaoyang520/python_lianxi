# -*- coding: utf-8 -*-

lst = [1,2,4,5,6,77,8]
s = {i for i in lst}
print(s)


lst1 = [1,3,4,4,6,5,3,2,2,2,8,2,2,1,1,1,1,3,54,5]
s1 = {i**2 for i in lst1}
print(s1)