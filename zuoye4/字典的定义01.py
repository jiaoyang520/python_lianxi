# 语法:变量名{k1:v1,k2:v2,kn:vn}
dict1 = {"name": "向阳", "age": "20", "hobby": ["听歌", "联盟"]}
print(dict1)
print(type(dict1))
# 注意:字典的key不能是可修改的数据类型,例如list列表就不可以，但是元组就可以
dict02 = {("name", "age"):"20"}
print(dict02)
