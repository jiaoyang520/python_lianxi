# 语法;{表达式1:表达式2 for .... in .....}
dict01 = {"a": 10, "b": 20}
new_dict01 = {}
for key, value in dict01.items():
    new_dict01[key] = value

print(new_dict01)

new_dict02 = {key: value for key, value in dict01.items()}
print(new_dict02)

dic01 = {k: v for k, v in zip(list("ABC"), list("123"))}
print(dic01)