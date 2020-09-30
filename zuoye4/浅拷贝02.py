def bianli(list01):
    i = 0
    while i < len(list01):
        if type(list01[i]) == tuple:
            print(f"第{i}个元素是: {list01[i]},类型是: {type(list01[i])},内存地址是: {id(list01[i])}")
            print(f"第{i}个中第0元素是: {list01[i][0]},内存地址是: {id(list01[i])}")
            print()
        elif type(list01[i]) == list:
            print(f"第{i}个元素是: {list01[i]},类型是: {type(list01[i])},内存地址是: {id(list01[i])}")
            print(f"第{i}个中第0元素是: {list01[i][0]},内存地址是: {id(list01[i])}")
            print()
        elif type(list01[i]) == dict:
            print(f"第{i}个元素是: {list01[i]},类型是: {type(list01[i])},内存地址是: {id(list01[i])}")
            for ii in list01[i].values():
                print(f"第{i}个中第0元素是: {ii},内存地址是: {id(ii)}")
                break
            print()
        elif type(list01[i]) == set:
            print(f"第{i}个元素是: {list01[i]},类型是: {type(list01[i])},内存地址是: {id(list01[i])}")
            for ii in list01[i]:
                print(f"第{i}个中第0元素是: {ii},内存地址是: {id(ii)}")
                break
            print()
        elif type(list01[i]) == str:
            print(f"第{i}个元素是: {list01[i]},类型是: {type(list01[i])},内存地址是: {id(list01[i])}")
            print()
        elif type(list01[i]) == int:
            print(f"第{i}个元素是: {list01[i]},内存地址是: {id(list01[i])}")
            print()
        i += 1



list01 = [("xy", 1), [2, 3], {"name": "xy"}, {6, 7}, "xiangyang", 1]

print("----------------------------------------------------------------")
bianli(list01)

print("----------------------------------------------------------------")
list02 = list01.copy()
bianli(list02)

print("----------------------------------------------------------------")
list03 = list01.copy()

bianli(list03)

# 总结:浅拷贝就是重新创建列表的内存地址，而元素的内存地址不变(同第一层的元素地址相同)
# 所以：浅拷贝就是新创建的列表内存地址指向第一层的元素地址
