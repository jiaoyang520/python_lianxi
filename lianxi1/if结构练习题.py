age = 18
if age >= 18:
    print("您已经到了18岁，可以上网了")

age = int(input("请输入你的年龄:"))
if 1 <= age <= 120:
    print("年龄输入正确")
else:
    print("年龄输入错误")

person1 = "有身份证"
person2 = "无身份证"
if person1 == "有身份证" or person2 == "有身份证":
    print("可以入住")
else:
    print("不可以入住")

is_student = "学生"
if is_student == "学生":
    print("可以进校园")
else:
    print("不可以进校园")

holiday_name = input("请输入节日名称:")
if holiday_name == "情人节":
    print("买鲜花，看电影")
elif holiday_name == "平安夜":
    print("买苹果，吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("关心女朋友")


has_ticket = "有车票"
knife_legth = 18
if holiday_name == "有车票" or 0 <= knife_legth <= 20:
    print("可以登车")
else:
    print("不让")

