# -*- coding: utf-8 -*-

dic = {"name":"贺凯","age":18,"address":"宁夏"}
# b = {for k,v }
for k,v in dic.items():
    print(k,v)

b = {v:k for k,v in dic.items()}
print(b)

c = {k:v for k,v in zip(list("bac"),list("123"))}
print(c)

