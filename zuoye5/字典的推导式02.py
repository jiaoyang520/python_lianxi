dict01 = {"a": 10, "b": 20}
new_dict01 = {key: value for key, value in dict01.items()}
print(new_dict01)

new_dict02 = {key: value for key, value in zip("abc", "123")}
print(new_dict02)