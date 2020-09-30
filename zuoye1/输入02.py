name = input("请输入姓名:")
print(name)

pwd = input("请输入密码:")
print(pwd)
print(type(pwd))

price = input("请输入购买香蕉的单价:")
weight = input("请输入购买香蕉的kg数:")
price = float(price)
weight = int(weight)
money = price * weight
print("您应付的钱数是:", money)