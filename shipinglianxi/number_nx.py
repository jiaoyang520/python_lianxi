# 整数
print(type(7))
print(type(7.77))
print(type(False))
# 整数加浮点转为浮点数
print(10+7.7, type(10+7.7))     # 17.7 <class 'float'>
# 数字类型的强制转换
    # int,float强转为bool型       0--->>False     非零--->>True
print(bool(0), type(bool(0)))       # False <class 'bool'>
print(bool(7), type(bool(7)))       # True <class 'bool'>
print(bool(0.0), type(bool(0.0)))    # False <class 'bool'>
print(bool(0.0007), type(bool(0.0007)))     # True <class 'bool'>
    # bool强转int,float      False--->>0      True--->>1
print(int(False), type(int(False)))       # 0 <class 'int'>
print(int(True), type(int(True)))       # 1 <class 'int'>
print(float(False), type(float(False))) # 0.0 <class 'float'>
print(float(True), type(float(True)))   # 1.0 <class 'float'>
    # int转float       会直接添加一个0的小数
print(float(10), type(float(10)))       # 10.0 <class 'float'>
    # float转int    会直接砍掉小数部分
print(int(7.77), type(int(7.77)))       # 7 <class 'int'>
# 自动升级      数字类型复杂度:   bool<int<float<complex
print(True+7, type(True+7))     # 8 <class 'int'>
print(True+7.77, type(True+7.7))        # 8.77 <class 'float'>