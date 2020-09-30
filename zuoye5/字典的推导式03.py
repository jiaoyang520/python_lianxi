dict01 = {"a": 10, "b": 20}
new_01 = {k: v for k, v in dict01.items()}
print(new_01)

new_02 = {k: v for k, v in zip("abcdefg","1234567")}
print(new_02)