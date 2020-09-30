import copy

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
            for ii, dd in list01[i].items():
                print(f"第{i}个中第0元素是: {ii,dd},内存地址是: {id(ii),id(dd)}")
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
list02 = copy.deepcopy(list01)
bianli(list02)

print("----------------------------------------------------------------")
list03 = copy.deepcopy(list01)
bianli(list03)

print("----------------------------------------------------------------")
list04 = copy.deepcopy(list01)
bianli(list04)

# 总结:深拷贝就是可变对象的内存地址改变(其中包括嵌套可变对象，而嵌套的不可变类型对象的地址不会发生改变），但是可变与不可变对象其中的元素内存地址不会改变，
