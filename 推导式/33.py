a = [i for i in range(10)]
print(a)

b = [i for i in range(1, 100, 2)]
print(b)

c = [i for i in range(2, 100, 2)]
print(c)

d = [i for i in range(200, 501) if i % 5 == 0 or i % 7 == 0]
print(d)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in lst:
    print(i)

i = 0
while i < len(lst):
    j = 0
    while j < len(lst):
        if j == i:
            print(lst[i][j])
        j += 1
    i += 1

f = [lst[i][2-i] for i in range(len(lst))]
print(f)

f2 = [lst[i][-i-1] for i in range(len(lst))]
print(f2)

lst = []
new_lst = []
count = 0
for i in range(1, 10):
    lst.append(i)
    count += 1
    if count  == 3:
        new_lst.append(lst)
        count = 0
        lst = []
print(new_lst)

lst = [i for i in range(1, 10)]
print(lst)
new_lst = [lst[j: j+3] for j in range(0, len(lst), 3)]
print(new_lst)

new_lsnew_lst = [[i for i in range(1, 10)][j: j+3] for j in range(0, len([i for i in range(1, 10)]), 3)]
print(new_lst)

new_lst = []
for i in range(3):
    lst = []
    for j in range(1, 4):
        lst.append(3*i+j)
    new_lst.append(lst)
print(new_lst)

f = [[3*j+i for i in range(1, 4) for j in range(3)]]
print(f)

dic = {"name":"贺凯","age":18,"address":"宁夏"}
for k, v in dic.items():
    print(k, v)

b = {v: k for k, v in dic.items()}
print(b)

lst = [1, 221, 412, 5, 6, 77, 8]
s = {i for i in lst}
print(s)

lst1 = [1, 3, 4, 4, 6, 5, 3, 2, 2, 2, 8, 2, 2, 1, 1, 1, 1, 3, 54, 5]
s1 = {i**2 for i in lst1}
print(s1)