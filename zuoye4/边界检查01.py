list01 = ["hello", 20, False]
#   查询列表超出列表边界则报错
print(list01[1])
# print(list01[7])        # 报错：IndexError: list index out of range     列表索引超出范围

#   给列表赋值超出列表的边界则报错
list01[7] = 77              # 报错：IndexError: list assignment index out of range 列表赋值索引超出范围
